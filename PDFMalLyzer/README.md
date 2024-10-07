# PDFMalLyzer

This program extracts 44 different features from a set of pdf files specified by the user and writes them on a csv file. The resulting csv file can be further studied for variety of purposes, most importantly for detecting malicious pdf files.

## Modules

pdf_feature_extractor.py is the main module which extracts a set of general and structural features. It utilizes the fitz library and the pdfid open source python tool.

## Prerequisites

This program runs on Linux operating systems only. It also requires an installation of python3 along with the fitz library. In order to run the program, navigate to the directory where the pdf_feature_extractor is. Then run the following command in the cmd, where the first argument is the path of a folder containing a set of pdf files.

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