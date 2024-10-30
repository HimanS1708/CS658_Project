import csv
import sys
import fitz
import os
import subprocess
import pandas as pd
import time
import os
import signal
from fitz import TextPage


import hashlib


import utils

def e():
        sys.exit(-1)

def usage():
      print("[-] Usage: python pdf_feature_extractor.py <path_containing_pdfs>")
      e()


if len(sys.argv) != 2: 
      usage()


dir = os.getcwd()
path = sys.argv[1]
if(not os.path.isabs(path)):      #if the given path is not absolute, we should convert it to one
         #print("the path is path is "+str(path))
         #print("dir is "+str(dir))
         path = os.path.join(dir,path)
         print("the path is not absolute and the new path is "+str(path))
if(os.path.isdir(path)):
        res = pd.DataFrame(columns=('pdfsize','metadata size', 'pages','xref length','title characters','isEncrypted','embedded files','images','contains text'))

else:
        print("specify a valid pdf folder path as an argument")
        sys.exit()
i = 0

def sig_handler(signum, frame):
    print("segfault")


md5_vals = []
for j in os.listdir(path):
        f = path + "/" + j
        # print("[+] Path: {}".format(f))
        #pdfFileObj = open(f,'rb')
        try:
                doc = fitz.open(f)
                #print("fitz "+str(doc.xrefLength))
                #file = open(f, 'rb')
        except:
                continue
        # print(doc.embfile_names())
        #metadata
        metadata = doc.metadata
        # print("metadata is "+str(metadata))

        #title
        if metadata:
                title = metadata['title']
        else:
                title = ""
        if not title:
                title = ""
        # print("title is "+str(title))

        #whether file is encrypted
        isEncrypted = -1
        if metadata:
                isEncrypted = metadata['encryption']
                if(not isEncrypted):
                        isEncrypted = 0
                else:
                        isEncrypted = 1
        #number of objects
        objects = doc.xref_length()
        # print("Object is " + str(objects))
                # print("object is "+str(object))

        # printing number of pages in pdf file
        numPages = doc.page_count
        # print("numpages is "+str(numPages))

        #extracted text
        pdfsize = int(os.path.getsize(f)/1000)
        # print("pdfsize is "+str(pdfsize))

        #extracted text
        found = "No"
        text = ""
        try:
                for page in doc:
                        text += page.get_text()
                        if (len(text) > 100):
                                found = "Yes"
                                break
        except:
         #       break
                 found = "unclear"
                 embedcount = doc.embfile_count()
                 res.loc[i] = [pdfsize, len(str(metadata).encode('utf-8'))] + [numPages] + [objects] + [len(title)] + [isEncrypted] + [embedcount] + [-1] + [found]
                 md5_vals.append(utils.md5sum(f))
                 i +=1
                 continue
                 
        #print("file contains text " + str(found))
        # number of embedded files
        embedcount = doc.embfile_count()
        # print("embedcount is "+str(embedcount))

        
        #number of images
        imgcount = 0
        try:
         for k in range(len(doc)):
               try:
                print(doc.get_images(k))
                imgcount = len(doc.get_images(k)) + imgcount
               except:  
                      continue
                 

        except:
         continue
        #print("image no is "+str(imgcount))




        #writing the features in a csv file
        res.loc[i] = [pdfsize, len(str(metadata).encode('utf-8'))] + [numPages] + [objects] + [len(title)] + [isEncrypted] + [embedcount] + [imgcount] + [found]
        md5_vals.append(utils.md5sum(f))
        i +=1
# Change the index of the dataframe
res = res.set_axis(md5_vals)
res.index.name = 'MD5'
res.to_csv(os.path.relpath("result.csv",start=os.curdir))
print("general features extracted successfully...")


print("extracting structural features...")        #extracting structural features using pdfid
var =  str(r"tr '\n' ','")
command = ""
header =  ['header', 'obj', 'endobj', 'stream', 'endstream', 'xref', 'trailer', 'startxref', 'pageno', 'Encrypt', 'ObjStm', 'JS', 'JavaScript', 'AA', 'OpenAction', 'AcroForm', 'JBIG2Decode', 'RichMedia', 'Launch', 'EmbeddedFile', 'XFA', 'URI', 'Colors', 'JS_Obfuscated', 'JavaScript_Obfuscated', 'AA_Obfuscated', 'OpenAction_Obfuscated', 'AcroForm_Obfuscated', 'JBIG2Decode_Obfuscated', 'RichMedia_Obfuscated', 'Launch_Obfuscated', 'EmbeddedFile_Obfuscated', 'XFA_Obfuscated', 'pageno_Obfuscated']
with open(os.path.relpath("pdfid/output.csv"),'w',encoding='UTF8') as output:
        output.write(','.join(header))
        # os.chdir('pdfid')
        t0 = time.time()
        for j in os.listdir(path):
                f = path + "/" + j
                try:
                       doc = fitz.open(f)
                except:
                       continue
                out = utils.pdfid(f)
                # print("==============================================")
                # print(out)
                # print("==============================================")
                out = list(out.values())
                # print("==============================================")
                # print(out[:23])
                # print("==============================================")
                print(len(out))
                print(len(header))
                out = ','.join(str(o) for o in out)
                output.write("\n" + out)
                d = time.time() - t0
        print("duration: %.2f s." % d)

custom_headers = ['%EOF','/Producer','/ProcSet','/ID','/S','/CreationDate','/Font','/XObject','/Widget','/FontDescriptor','/Rect','/ModDate','/Info','/XML','dict_start','dict_end','comments','custom_metadata','metadata_stream','page_rotation']
with open(os.path.relpath("output2.csv"), 'w', encoding='UTF8') as output:
        output.write(','.join(custom_headers))

        print("\n\n\nExtracting Custom headers!!!\n\n\n")
        t0 = time.time()

        for j in os.listdir(path):
                f = path + "/" + j
                # if not j.lower().endswith('.pdf'):
                #     continue
                try: 
                       doc = fitz.open(f)
                except:
                       continue

                out = utils.pdfcust(f)
                out = list(out.values())
                out = ','.join(str(o) for o in out)
                output.write("\n" + out)
        
        t1 = time.time()
        print("\nDuration: %.2f s.\n" % (t1-t0))
       

print("Finished extracting custom features!!!")
# os.system("paste result.csv pdfid/output.csv > output1.csv")
# os.system("paste output1.csv output2.csv > output.csv")

df1 = pd.read_csv("result.csv")
df2 = pd.read_csv("pdfid/output.csv")
df3 = pd.read_csv("output2.csv")

combined_df = pd.concat([df1, df2, df3], axis=1)

combined_df.to_csv("output.csv", index=False)

os.remove("pdfid/output.csv")
os.remove("output2.csv")
os.remove("result.csv")









