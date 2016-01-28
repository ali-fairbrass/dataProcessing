
import os
import csv

CSV_DIR = 'Y:\\Fieldwork_Data\\2015\\Random_25\\SM2+labels'

csvFiles = os.listdir(CSV_DIR)

labelList = []
for csvFile in csvFiles:
    filePath = CSV_DIR + '\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
        	labelList.append(row[1])

labelListNoDuplicates = list(set(labelList))

print labelListNoDuplicates