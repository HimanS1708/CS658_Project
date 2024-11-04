# PDFMalLyzer

This program extracts **61** different features from a set of pdf files specified by the user and writes them on a csv file. The resulting csv file can be further studied for a variety of purposes, most importantly for detecting malicious pdf files.

## Modules

**pdf_feature_extractor.py** is the main module which extracts a set of general and structural features. It utilizes the fitz library, the pdfid open source python tool and the PyPDF2 library for feature extraction.

**make_csv.sh** is the bash script that downloads the entire dataset in the "../Dataset/" directory. The details of the dataset are mentioned in the main project directory.

## Prerequisites

This program runs on Linux operating systems only or in a WSL. It also requires an installation of python3. In order to run the program, navigate to the directory where the **pdf_feature_extractor.py** is. Then run the following command on the terminal, where the first argument is the path of a folder containing a set of pdf files.

```
python3 pdf_feature_extractor.py pdf-folder-path
```

If the pre-requisite packages are not installed, make sure to run the following commands before executing the script. 

```
pip install -r requirements.txt
```
OR
```
pip3 install -r requirements.txt
```

## Features

- MD5 - A cryptographic hash used to uniquely identify PDF files

### Standard Features

- pdfsize - Size of the PDF file in kilobytes (KB)
- metadata - Size of the PDF's metadata in bytes when encoded in UTF-8
- pages - Total number of pages in the PDF
- xref length - Length of the cross-reference (xref) table in a PDF document
- title characters - Length of the PDF document's title from its metadata
- isEncrypted - Binary indicator that shows whether a PDF file is encrypted or not
- embedded files - Number of embedded files within a PDF document (.exe, .jpg, .js etc.)
- images - Total number of images contained within a PDF document
- contains text - Categorical indicator ("Yes", "No" or "Unclear") that shows whether a PDF contains readable text content

### Structural Features

- header - Represents the PDF version identifier from the PDF file header
- obj - Count of object declarations in a PDF file (fonts, text, images etc.)
- endobj - Count of termination keywords for every object declaration in a PDF file
- stream - Count of stream objects in PDFs, used to hold binary data. (fonts, images etc.)
- endstream - Count of termination keywords for every stream declaration in a PDF file
- xref - Count of cross-reference tables in a PDF file
- trailer - Count of trailer dictionaries in a PDF file
- startxref - Count of startxref markers in a PDF file
- pageno - Total number of pages in the PDF
- Encrypt - Count of encryption dictionary entries in a PDF file
- ObjStm - Count of object stream entries in a PDF file (allows multiple objects to be compressed together into a single stream)
- JS - Count of /JS keywords which reveals the objects having Javascript code
- JavaScript - Count of /JavaScript entries in a PDF file (common and prevalent obfuscation technique)
- AA - Count of /AA keywords in a PDF file (can execute certain events)
- OpenAction - Count of /OpenAction keywords in a PDF file (action that is automatically executed when the PDF is opened)
- AcroForm - Count of /AcroForm keywords (interactive form fields in PDFs like text fields, buttons etc.)
- JBIG2Decode - Count of /JBIG2Decode keywords (a compression algorithm for bi-level black and white images)
- RichMedia - Count of /RichMedia keywords (interactive or multimedia content)
- Launch - Count of /Launch keywords (launch or execute external applications)
- EmbeddedFile - Count of /EmbeddedFile keywords (.exe, .js, etc.)
- XFA - Count of /XFA keywords (XML Form Architectures that offer scripting capabilities)
- URI - Count of /URI keywords (used for linking to external resources or websites)
- Colors - Number of different colors utilized in the PDF structure
- JS_Obfuscated - Malformed instances of /JS keywords
- JavaScript_Obfuscated - Malformed instances of /JavaScript keywords 
- AA_Obfuscated - Malformed instances of /AA keywords
- OpenAction_Obfuscated - Malformed instances of /OpenAction keywords
- AcroForm_Obfuscated - Malformed instances of /AcroForm keywords
- JBIG2Decode_Obfuscated - Malformed instances of /JBIG2Decode keywords
- RichMedia_Obfuscated - Malformed instances of /RichMedia keywords
- Launch_Obfuscated - Malformed instances of /Launch keywords
- EmbeddedFile_Obfuscated - Malformed instances of /EmbeddedFile keywords
- XFA_Obfuscated - Malformed instances of /XFA keywords
- pageno_Obfuscated - Malformed instances of /Page keywords

### Custom Features for exploration
- %EOF - Count of %EOF keywords in the PDF
- /Producer - Count of /Producer keywords in the PDF (tool or software by which the PDF was created)
- /ProcSet - Count of /ProcSet keywords in the PDF (set of procedures that must be employed while rendering a page or graphic content)
- /ID - Count of /ID keywords in the PDF (document ID)
- /S - Count of /S keywords in the PDF (subtype of objects like text or link annotations)
- /CreationDate - Count of /CreationDate keywords in the PDF
- /Font - Count of /Font keywords in the PDF
- /XObject - Count of /XObject keywords in the PDF
- /Widget - Count of /Widget keywords in the PDF (used for form field elements like buttons, text fields etc.)
- /FontDescriptor - Count of /FontDescriptor keywords in the PDF (contains font metrics and characteristics)
- /Rect - Count of /Rect keywords in the PDF (defines rectangular boundaries for annotations and form fields)
- /ModDate - Count of /ModDate keywords in the PDF (indicates when the document was last modified)  
- /Info - Count of /Info keywords in the PDF (contains document information dictionary)
- /XML - Count of /XML keywords in the PDF (indicates XML data structures within the document)
- dict_start - Count of '<<' keywords in the PDF (signifies start of a dictionary object)
- dict_end - Count of '<<' keywords in the PDF (signifies end of a dictionary object)
- comments - Count of comment markers (lines starting with %) within the PDF file

## Others

**test_utils.py** and **utils.py** are helper scripts used by the **pdf_feature_extractor.py** file.

**tests** is just a dummy directory with 2 PDFs which can be used for testing.

**Extracts** directory stores the final csv for the entire dataset.

**pdfid** contains the helper files.