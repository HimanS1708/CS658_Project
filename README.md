# CS658 Project

This is the project repository of Group 5 for the course CS658. We are working on the **CIC-Evasive-PDFMal2022** dataset. Our project idea is inspired by the paper [“PDF Malware Detection Based on Stacking Learning”](https://pdfs.semanticscholar.org/c4e6/1e9545951bf4e7dbefd7796b6f7f050a75f6.pdf), The International Conference on Information Systems Security and Privacy, February 2022. The goal of this project is to update the dataset with data post 2022 and review the ML/DL model used and try out modern techniques for classification.

## PDF Dataset

Available [here](http://205.174.165.80/CICDataset/CIC-EvasivePDF2022/Dataset/): 9107 Benign files and 21721 Malicious files

TODO: Get recent data from places like MalwareBazaar or other open source repositories providing malicious PDFs.

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

Currently we are only using the RandomForest model with n_estimators = 50, max_depth = 500 and max_features = log2

TODO: Create a stacking learning model as implemented in the paper and try out different base and meta learners.

## Team

Himanshu Shekhar (220454)

Lokesh Yadav (220594)

Kamal Kant Tripathi (241110086)