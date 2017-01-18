import os
import csv

CSV_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\extra25BioticLabels'

csvFiles = os.listdir(CSV_DIR)

csvList = []
for csvFile in csvFiles:
    filePath = CSV_DIR + '\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
        	if row[1] == "Insect":
        		csvList.append(csvFile[:-14])

csvListNoDuplicates = list(set(csvList))
print csvListNoDuplicates
csvList = []

for csvFile in csvListNoDuplicates:
	csvList.append([csvFile])

print csvList

CSV_DIR = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3\\secondTraining\\"

with open(CSV_DIR + "2014And2015_second25_invertebrate.csv", 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(['Filename'])
    for row in csvList:
        wr.writerow(row)