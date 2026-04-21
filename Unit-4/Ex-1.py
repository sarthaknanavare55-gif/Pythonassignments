import csv 

row_count=0

with open("/Users/naitikwautre/Downloads/Book(Sheet1).csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        row_count +=1
print("Tota number of rows:", row_count)        