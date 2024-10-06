#!/bin/bash

benign_directory="../Dataset/Benign/"
benign_placeholder="Ben0"

malicious1_directory="../Dataset/Malicious/"
malicious1_placeholder="f"

if [ ! -d "Extracts" ]; then
    mkdir -p "Extracts"
    mkdir -p "Extracts/Benign"
    mkdir -p "Extracts/Malicious"
fi

echo "========================="
echo
echo "Starting Benign Files extraction"
echo
for i in {1..9}
do
    result="$benign_directory$benign_placeholder$i"
    # echo $result
    python3 pdf_feature_extractor.py $result

    csv_directory="./Extracts/Benign"
    csv_name="$benign_placeholder$i.csv"
    cp output1.csv $csv_name
    rm output1.csv
    mv $csv_name $csv_directory
done
echo
echo "Benign Files extraction done!"
echo
echo "========================="
echo

echo
echo "========================="
echo
echo "Starting Malicious Files extraction"
echo
for i in {1..22}
do
    result="$malicious1_directory$malicious1_placeholder$i"
    # echo $result
    python3 pdf_feature_extractor.py $result

    csv_directory="./Extracts/Malicious"
    csv_name="$malicious1_placeholder$i.csv"
    cp output1.csv $csv_name
    rm output1.csv
    mv $csv_name $csv_directory
done
echo
echo "Malicious Files extraction done!"
echo
echo "========================="
echo
