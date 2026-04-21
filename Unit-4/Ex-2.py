import json
import csv
try:
    with open("\Documents\Python Lab\Unit 4\Convert.py","r") as json_file:
        data=json.load(json_file)

    with open('output.csv','w',newline='') as csv_file:
        headers=data[0].keys()
        writer=csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print("Conversion successful!")
except FileNotFoundError:
    print("Error: Data.json file not found. Check file path.")