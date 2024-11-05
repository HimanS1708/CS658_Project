## Installing the libraries

Install the required libraries by running the following command -

```
pip install -r requirements.txt
```
OR
```
pip3 install -r requirements.txt
```

## Working

The ```make_final_csv.py``` file is for creating the final csv. Make sure that the individual csv files (containing the features only) are in ```../PDFMalLyzer/Benign/```, ```../PDFMalLyzer/Malicious/```, ```../PDFMalLyzer/GOVDocs/``` and ```../PDFMalLyzer/VirusShare```. The individual csv files are combined and stored in the current directory as ```final.csv```. To run the code -

```
python make_final_csv.py
```
OR
```
python3 make_final_csv.py
```
\
\
The ```main.ipynb``` notebook contains some analysis of the features.