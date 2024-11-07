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

## Descriptions

The ```features.ipynb``` notebook contains some analysis of the features.
\
\
The ```Paper_Model.ipynb``` notebook contains the model proposed in the original paper. We tried playing around with some parameters and tested it on various configurations.
\
\
The ```SHAP_Balanced.ipynb``` notebook contains the performance of various models under a balanced training dataset.
\
\
The ```SHAP_Imbalanced.ipynb``` notebook contains the performance of various models without balancing the training dataset.
\
\
**Observations**: The model worked better when using a balanced dataset. Also, XGBoost seemed to outperform all other models based on both **time to execute** and **accuracy**.
\
\
The ```SHAP_XGB.ipynb``` notebook contains various features analysis and model performance when using XGBoost with Hyperparameter tuning and Feature selection.