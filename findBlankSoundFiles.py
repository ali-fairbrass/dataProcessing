import os
import shutil
import random

# CSV_DIR_NO_TRANSPORT = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\LabelsCSV\\'
# CSV_DIR_TRANSPORT24kHz = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\LabelsCSVTransport\\24000HzSR'
# CSV_DIR_TRANSPORT41kHz = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\LabelsCSVTransport\\41000HzSR'
CSV_DIR = 'Y:\\Fieldwork_Data\\2015\\Random_25\\SM2+_VerityLabels\\'
WAV_DIR = 'Y:\\Fieldwork_Data\\2015\\Random_25\\SM2+_downSample\\'

# csvFilesNoTransport = os.listdir(CSV_DIR_NO_TRANSPORT)
# csvFilesTransport24kHz = os.listdir(CSV_DIR_TRANSPORT24kHz)
# csvFilesTransport41kHz = os.listdir(CSV_DIR_TRANSPORT41kHz)
csvFiles = os.listdir(CSV_DIR)
wavFiles = os.listdir(WAV_DIR)

csvFileList = []
for csvFile in csvFiles:
    csvBaseName = csvFile[:-14]
    csvFileList.append(csvBaseName)

# for csvFile in csvFilesTransport24kHz:
#     csvBaseName = csvFile[:-14]
#     csvFileList.append(csvBaseName) 

# for csvFile in csvFilesTransport41kHz:
#     csvBaseName = csvFile[:-14]
#     csvFileList.append(csvBaseName)

# csvFileList =  list(set(csvFileList)) 
  
wavFileList = []
for wavFile in wavFiles:
    wavBaseName = wavFile[:-4]
    wavFileList.append(wavBaseName)

wavWOcsv = []
for wav in wavFileList:
    if wav not in csvFileList:
        wavWOcsv.append(wav)

verityLabels = []
for wavFile in wavWOcsv:
    if wavFile[:3] in ('BR4', 'BR2', 'IG6', 'E29', 'TW7', 'BR6', 'DA5', 'RM4', 'CM1'):
        verityLabels.append(wavFile)

# print verityLabels

# dirExtention = "C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\Amalgamated_Files_24kHz\\"
# fileList = os.listdir(WAV_DIR)

# wav2FileList = []
# for wav2 in fileList:
# 	wav2BaseName = wav2[:-4]
# 	wav2FileList.append(wav2BaseName)

fileListBlankFiles = [x for x in wavFileList if x in verityLabels]

print len(fileListBlankFiles)

randomNumbers = random.sample(xrange(len(fileListBlankFiles)), 2)
fileSelection = [fileListBlankFiles[i] for i in randomNumbers]

print fileSelection

for i in fileSelection:
    shutil.copy(WAV_DIR + i + '.wav', "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 3\\goldenTestSet\\21VerityFiles")


