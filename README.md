# CS658 Project

This is the project repository of Group 5 for the course CS658. We are working on the **CIC-Evasive-PDFMal2022** dataset. Our project idea is inspired by the paper [“PDF Malware Detection Based on Stacking Learning”](https://pdfs.semanticscholar.org/c4e6/1e9545951bf4e7dbefd7796b6f7f050a75f6.pdf), The International Conference on Information Systems Security and Privacy, February 2022. The goal of this project is to update the dataset with data post 2022 and review the ML/DL model used and try out modern techniques for classification. A thorough analysis of the existing dataset and model has been carried out to identify the limitations and finding the innovative ways to overcome the same. 

## PDF Dataset

Available [here](http://205.174.165.80/CICDataset/CIC-EvasivePDF2022/Dataset/): 9107 Benign files and 21721 Malicious files. In addition to this existing dataset from CIC Website, we have added a diverse dataset obtained from VirusShare, GOVDocs, PDFRep, VirusTotal etc. The dataset contains equal proportion of malicious and benign PDF files making a balanced and robust set of data to test and validate our improved version of Model. The following three novel idesa have been implemented in this project:-
    1. Enhanced Dataset
    2. Enhanced Feature set
    3. Implementation of SHAP (SHapley Additive exPlanations)

## Feature Extraction

For feature extraction from the PDFs, we used the [PDFMalLyzer](https://github.com/ahlashkari/PDFMalLyzer) tool. This tool is very outdated and also produces incorrect results for the given dataset. The code was updated and the required dependencies are also provided in the directory. 

## Repository Structure

| Directory       | Description |
|-----------------|-------------|
| Analysis        | Contains the analysis of different features, their counts and distributions for both benign and malicious PDFs   |
| Experimentation | Contains random experimentation code that was written for trying out different libraries etc.  |
| Model           | Contains the ML model that classifies the PDF files  |
| PDFMalLyzer     | Contains the corrected feature extractor tool for extracting features from a PDF file |
| Write_ups       | Contains the write ups that were to be submitted for the project |

## Models

Created a stacking classifier model with MLP, RandomForest and SVM as Base learners and a Logistic Regression model as Meta Learner.

Hyperparameters used -

* RandomForestClassifier - n_estimators=200, max_depth=20, min_samples_leaf=1, min_samples_split=2, random_state=42
* MLPClassifier - hidden_layer_sizes=(100,), max_iter=1000, activation='tanh', learning_rate_init=0.001, random_state=42
* SVC - C=100, kernel='rbf', gamma='scale', probability=True, random_state=42
* LogisticRegression - random_state=42

## Team

Himanshu Shekhar (220454)

Lokesh Yadav (220594)

Kamal Kant Tripathi (241110086)
