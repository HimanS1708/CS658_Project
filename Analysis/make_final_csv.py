import pandas as pd
import os

path = '../PDFMalLyzer/Extracts/Benign/'

csv_files = [f for f in os.listdir(path) if f.startswith('Ben') and f.endswith('.csv')]

combined_csv = pd.concat([pd.read_csv(os.path.join(path, f)) for f in csv_files])

combined_csv.to_csv('benign.csv', index=False)

print("CSV files combined successfully into benign.csv")

path = '../PDFMalLyzer/Extracts/Malicious/'

csv_files = [f for f in os.listdir(path) if f.startswith('f') and f.endswith('.csv')]

combined_csv = pd.concat([pd.read_csv(os.path.join(path, f)) for f in csv_files])

combined_csv.to_csv('malicious.csv', index=False)

print("CSV files combined successfully into malicious.csv")

benign = pd.read_csv('benign.csv')
malicious = pd.read_csv('malicious.csv')
gov = pd.read_csv('../PDFMalLyzer/Extracts/GOVDocs/GOVDocs_300_to_399.csv')
vs = pd.read_csv('../PDFMalLyzer/Extracts/VirusShare/VirusShare.csv')

benign['Malicious'] = 'No'
gov['Malicious'] = 'No'
malicious['Malicious'] = 'Yes'
vs['Malicious'] = 'Yes'

combined_csv = pd.concat([benign, malicious, gov, vs])

combined_csv = combined_csv.sample(frac=1).reset_index(drop=True)

combined_csv.to_csv('final.csv', index=False)

print("Files merged successfully")

os.remove('benign.csv')
os.remove('malicious.csv')