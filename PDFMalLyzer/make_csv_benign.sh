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

# echo "========================="
# echo
# echo "Starting Benign Files extraction"
# echo
# for i in {1..9}
# do
#     result="$benign_directory$benign_placeholder$i"
#     # echo $result
#     python3 pdf_feature_extractor.py $result

#     csv_directory="./Extracts/Benign"
#     csv_name="$benign_placeholder$i.csv"
#     cp output.csv $csv_name
#     rm output.csv
#     mv $csv_name $csv_directory
# done
# echo
# echo "Benign Files extraction done!"
# echo
# echo "========================="
# echo

# echo
# echo "========================="
# echo
# echo "Starting Malicious Files extraction"
# echo
# for i in {1..22}
# do
#     result="$malicious1_directory$malicious1_placeholder$i"
#     # echo $result
#     python3 pdf_feature_extractor.py $result

#     csv_directory="./Extracts/Malicious"
#     csv_name="$malicious1_placeholder$i.csv"
#     cp output.csv $csv_name
#     rm output.csv
#     mv $csv_name $csv_directory
# done
# echo
# echo "Malicious Files extraction done!"
# echo
# echo "========================="
# echo

echo
echo "========================="
echo
echo "Downloading GOVDocs dataset..."
echo
mkdir -p "../Dataset/GOVDocs"
for i in {000..399}
do
    aria2c -x 16 --dir="../Dataset/GOVDocs" "https://digitalcorpora.s3.amazonaws.com/corpora/files/govdocs1/zipfiles/$i.zip"
done
echo
echo "Downloading GOVDocs complete!"
echo
echo "========================="
echo

echo
echo "========================="
echo
echo "Extracting zip file..."
echo
unzip "../Dataset/GOVDocs/*.zip" -d "../Dataset/GOVDocs"
rm "../Dataset/GOVDocs/*.zip"
echo
echo "Extraction complete!" 
echo
echo "========================="
echo

echo
echo "========================="
echo
echo "Cleaning GOVDocs Files"
echo
for i in {000..399}
do
    result="../Dataset/GOVDocs/$i"
    find "$result" -type f ! -name "*.pdf" -delete
done
echo
echo "========================="
echo
echo "Cleaning done!"

echo
echo "========================="
echo
echo "Starting GOVDocs Files extraction"
echo
for i in {000..399}
do
    result="../Dataset/GOVDocs/$i"
    python3 pdf_feature_extractor.py $result

    csv_directory="./Extracts/GOVDocs"
    mkdir -p $csv_directory
    csv_name="GOVDoc$i.csv"
    cp output.csv $csv_name
    rm output.csv
    mv $csv_name $csv_directory
done
echo
echo "GOVDocs Files extraction done!" 
echo
echo "========================="
echo
