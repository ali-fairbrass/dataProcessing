
import os
import csv

CSV_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\extra25BioticLabels'

csvFiles = os.listdir(CSV_DIR)

labelList = []
for csvFile in csvFiles:
    filePath = CSV_DIR + '\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
        	labelList.append(row[1])

labelListNoDuplicates = list(set(labelList))

print sorted(labelListNoDuplicates)