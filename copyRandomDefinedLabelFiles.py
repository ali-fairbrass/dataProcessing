import os
import csv
import shutil
import random

CSV_DIR = 'Y:\\Fieldwork_Data\\2015\\Random_25\\SM2+_VerityLabels'
WAV_DIR = 'Y:\\Fieldwork_Data\\2015\\Random_25\\SM2+_downSample'
csvFiles = os.listdir(CSV_DIR)
wavFiles = os.listdir(WAV_DIR)

# labelList = []
# for csvFile in csvFiles:
#     filePath = CSV_DIR + '\\' + csvFile
#     with open(filePath, 'rb') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             labelList.append(row[1])

# print list(set(labelList))

bioticFileList = []
for csvFile in csvFiles:
    filePath = CSV_DIR + '\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] in ('Squirrel', 'animal', 'bird', 'invertebrate', 'russling leaves (animal)'):
                bioticFileList.append(csvFile)


bioticFileListNoDuplicates = list(set(bioticFileList))

csvBaseList = []
for fileName in bioticFileListNoDuplicates:
    csvBaseName = fileName[:-14]
    csvBaseList.append(csvBaseName)
    
wavFileList = []
for wavFile in wavFiles:
    wavBaseName = wavFile[:-4]
    wavFileList.append(wavBaseName)

fileListBiotic = [x for x in wavFileList if x in csvBaseList]

randomNumbers = random.sample(xrange(len(fileListBiotic)), 19)
fileSelection = [fileListBiotic[i] for i in randomNumbers]

for i in fileSelection:
    print "Copying file: " + i
    shutil.copy(WAV_DIR + '\\' + i + '.wav', "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 3\\goldenTestSet\\21VerityFiles")