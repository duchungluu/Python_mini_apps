# Access file server 
python3 -m http.server

#get ipconfig 192.168.x.x


# Convert csv to json
python -c "import csv,json;print json.dumps(list(csv.reader(open('your_csv_file.csv'))))"