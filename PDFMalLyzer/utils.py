# python pdfid.py /Users/gx1/git/secsi/PDFMalLyzer/tests/small_file/02solp.pdf

import hashlib
import os
import subprocess

import re
from typing import Dict, Union
import json

import PyPDF2
from io import BytesIO

var =  str(r"tr '\n' ','")

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()




def md5sum(f):
    md5_hash = hashlib.md5()
    with open(f, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        return md5_hash.hexdigest()


def pfid_cmd(f):
    return "python3 pdfid.py \"" + f + "\""

# Valid PDF versions
PDF_VALID_VERSIONS = [
    '%PDF-1.0',
    '%PDF-1.1',
    '%PDF-1.2',
    '%PDF-1.3',
    '%PDF-1.4',
    '%PDF-1.5',
    '%PDF-1.6',
    '%PDF-1.7',    
    '%PDF-2.0'
]

def parse_header(s):
    print(s.split(":"))
    ret = s.split(":")[1].strip()
    return ret if ret in PDF_VALID_VERSIONS else 'Malformed'

def _obfuscated_fields(ret):
    FIELDS = ['/Page', '/JS', '/JavaScript', '/AA', '/OpenAction', '/AcroForm', '/JBIG2Decode', '/RichMedia', '/Launch', '/EmbeddedFile', '/XFA']
    for f in FIELDS:
        # Get the value
        val = ret[f]
        # If it is integer, simply remain the value and adds the obfuscation to 0
        if is_integer(val):
            ret["{}_Obfuscated".format(f)] = 0
        # It meas that the number is in form 2(1) where 2 is the number of elements and 1 the number of obfuscations
        else: 
           splitted_val = val.split('(')
           # Take 2(1) and create a new key for the obfuscation and change that of the object
           no_objects = splitted_val[0]
           no_obfusc  = splitted_val[1].replace(")", "")
           ret[f] = no_objects
           ret["{}_Obfuscated".format(f)] = no_obfusc

    return ret

def _clean_ret(ret):
    ret = _obfuscated_fields(ret)
    clean_ret = {key.replace("/", "").strip() if key != 'header' else key: int(item) if key != 'header' else item.strip() for key, item in ret.items()}
    # Replace name
    clean_ret['pageno'] = clean_ret.pop('Page')
    clean_ret['pageno_Obfuscated'] = clean_ret.pop('Page_Obfuscated')

    return clean_ret

def pdfid(f):
    """Call the Steven script to obtain the structural features

    Args:
        filename (str): the full path filename
    """
    the_cmd = pfid_cmd(f)
    print("[+] {}".format(the_cmd))
    os.chdir('pdfid')
    ret = {}
    out = subprocess.getoutput(the_cmd)
    print(out)
    splitted_lines = out.split("\n")[1:]
    print(splitted_lines)
    header = parse_header(splitted_lines[0])
    ret['header'] = header
    splitted_lines = splitted_lines[1:]
    for s in splitted_lines: 
        s_arr = s.split()
        if len(s_arr):
            if not s_arr[0].startswith('/Colors'):
                ret[s_arr[0]] = s_arr[1]
            else:
                ret[s_arr[0]] = s_arr[3]

    os.chdir('../')
    clean_ret  = _clean_ret(ret)
    return clean_ret

class PDFFeatureExtractor:
    """
    A class to extract features from PDF files for malware detection.
    """
    
    def __init__(self, pdf_path: str):
        """Initialize with path to PDF file."""
        self.pdf_path = pdf_path
        self.raw_content = None
        self.pdf_size_kb = None
        self._load_pdf()

    # def _is_pdf_content(self, content: bytes) -> bool:
    #     """Check if content appears to be PDF data"""
    #     # Check for PDF magic number
    #     return content.startswith(b'%PDF-')

    def _load_pdf(self) -> None:
        """Load the PDF file and store its raw content."""
        try:
            # Get file size in KB
            self.pdf_size_kb = os.path.getsize(self.pdf_path) / 1024

            # Read raw content
            with open(self.pdf_path, 'rb') as file:
                self.raw_content = file.read()
                
        except Exception as e:
            raise Exception(f"Error loading PDF: {str(e)}")

    def _count_keyword(self, keyword: str) -> int:
        """Count occurrences of a keyword in the PDF content."""
        return len(re.findall(bytes(keyword, 'utf-8'), self.raw_content))

    def extract_features(self) -> Dict[str, Union[int, str, bool]]:
        """Extract all relevant features from the PDF."""
        features = {}
        
        # Basic structure keywords
        # structure_keywords = [
        #     'obj', 'endobj', 'stream', 'endstream', 'xref', 'trailer',
        #     'startxref', '/Page', '/Encrypt', '/Size', '%EOF', '/Producer',
        #     '/ProcSet', '/ID', '/S', '/CreationDate'
        # ]
        structure_keywords = ['%EOF','/Producer','/ProcSet','/ID','/S','/CreationDate']
        
        for keyword in structure_keywords:
            features[keyword] = self._count_keyword(keyword)

        # JavaScript and action-related features
        # js_keywords = [
        #     '/JS', '/JavaScript', '/AA', '/OpenAction', '/AcroForm',
        #     '/Launch', '/Action'
        # ]
        js_keywords = []
        
        for keyword in js_keywords:
            features[keyword] = self._count_keyword(keyword)

        # Media and embedded content features
        # media_keywords = [
        #     '/JBIG2Decode', '/RichMedia', '/EmbeddedFIle', '/XFA',
        #     '/Font', '/XObject', '/Image'
        # ]
        media_keywords = ['/Font','/XObject']
        
        for keyword in media_keywords:
            features[keyword] = self._count_keyword(keyword)

        # Additional structural elements
        # additional_keywords = [
        #     '/Widget', '/FontDescriptor', '/Rect', '/Length',
        #     '/ModDate', '/Info', '/XML'
        # ]
        additional_keywords = ['/Widget','/FontDescriptor','/Rect','/ModDate','/Info','/XML']
        
        for keyword in additional_keywords:
            features[keyword] = self._count_keyword(keyword)

        # Special characters
        features['dict_start'] = self._count_keyword('<<')
        features['dict_end'] = self._count_keyword('>>')
        features['comments'] = len(re.findall(b'%[^\n]*\n', self.raw_content))

        # File metadata
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                # print(pdf_reader)
                
                # features['page_count'] = len(pdf_reader.pages)
                metadata = pdf_reader.metadata
                features['custom_metadata'] = 'yes' if metadata and len(metadata)>0 else 'no'

                try:
                    if hasattr(pdf_reader, 'trailer'):
                        features['metadata_stream'] = 'yes' if pdf_reader.trailer.get('/Metadata') else 'no'
                    else:
                        features['metadata_stream'] = 'no'
                except:
                    features['metadata_stream'] = 'no'
                # features['file_size_kb'] = self.pdf_size_kb
                # features['pdf_version'] = self._get_pdf_version()
                
                # Check for forms
                # features['has_acroform'] = hasattr(pdf_reader, 'acroform')
                
                # Check for XFA forms
                # if features['has_acroform'] and pdf_reader.acroform:
                #     features['form_type'] = 'XFA' if '/XFA' in str(pdf_reader.acroform) else 'AcroForm'
                # else:
                #     features['form_type'] = 'none'
                
                # Get first page size
                if len(pdf_reader.pages) > 0:
                    page = pdf_reader.pages[0]
                #     if '/MediaBox' in page:
                #         mediabox = page['/MediaBox']
                #         width, height = float(mediabox[2]), float(mediabox[3])
                #         features['page_size'] = f"{width}x{height}"
                #     else:
                #         features['page_size'] = "unknown"
                    
                #     # Page rotation
                    features['page_rotation'] = page.get('/Rotate', 0)
                
        except Exception as e:
            print(f"Warning: Error extracting PyPDF2 features: {str(e)}")
            features.update({
                'custom_metada': 'no',
                'metadata_stream': 'no',
                # 'form_type': 'unknown',
                # 'page_size': 'unknown',
                'page_rotation': 0
            })

        return features

def analyze_pdf(pdf_path: str) -> Dict[str, Union[int, str, bool]]:
    """
    Analyze a PDF file and extract all relevant features.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Dictionary containing all extracted features
    """
    extractor = PDFFeatureExtractor(pdf_path)
    return extractor.extract_features()

def pdfcust(f):
    """Call this function to extract custom headers
    
    Args:
        filename (str): the full path filename
    """
    try:
        features = analyze_pdf(f)
        print(json.dumps(features, indent=2))
        return features
    except Exception as e:
        print(f"Error analyzing PDF {f}: {str(e)}")
