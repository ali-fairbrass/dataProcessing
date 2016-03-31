import os
import csv
import shutil


CSV_DIR = 'Y:\\Fieldwork_Data\\2015\\Random_25\\SM2+_VerityLabels'
WAV_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 3\\goldenTestSet\\21VerityFiles'
csvFiles = os.listdir(CSV_DIR)
wavFiles = os.listdir(WAV_DIR)
    
csvFileList = []
for wavFile in wavFiles:
    wavBaseName = wavFile[:-4]
    csvName = wavBaseName + '-sceneRect.csv'
    csvFileList.append(csvName)

#Remove blank files
csvFileList.remove('BR4-013378_20150820_22000018-sceneRect.csv')
csvFileList.remove('E29RR-013378_20150530_03000023-sceneRect.csv')

for i in csvFileList:
    print "Copying file: " + i
    shutil.copy(CSV_DIR + '\\' + i, "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 3\\goldenTestSet\\21VerityLabels")
