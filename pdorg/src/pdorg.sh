#!/bin/sh
echo "pdorg currently requires you have a Pictures folder in your
home/user directory"
cd
cd "Pictures/"
>temp_data.txt
for i in *; do exiftool -common $i >>temp_data.txt; done
cd "pdorg/src"
python3 "pdorg.py"
echo "phase 2"
python3 "pdorg2.py"
cd "../../"
echo "Images without metadata will be put in a seperate folder from the rest"
find -name '*IMG*' -exec mv -t "snapchat" {} +
rm "temp_data.txt"