import os
import shutil
import random

CSV_DIR_NO_TRANSPORT = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\LabelsCSV\\'
CSV_DIR_TRANSPORT24kHz = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\LabelsCSVTransport\\24000HzSR'
CSV_DIR_TRANSPORT41kHz = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\LabelsCSVTransport\\41000HzSR'
WAV_DIR = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\Amalgamated_Files_24kHz\\'

csvFilesNoTransport = os.listdir(CSV_DIR_NO_TRANSPORT)
csvFilesTransport24kHz = os.listdir(CSV_DIR_TRANSPORT24kHz)
csvFilesTransport41kHz = os.listdir(CSV_DIR_TRANSPORT41kHz)
wavFiles = os.listdir(WAV_DIR)

csvFileList = []
for csvFile in csvFilesNoTransport:
    csvBaseName = csvFile[:-14]
    csvFileList.append(csvBaseName)

for csvFile in csvFilesTransport24kHz:
    csvBaseName = csvFile[:-14]
    csvFileList.append(csvBaseName) 

for csvFile in csvFilesTransport41kHz:
    csvBaseName = csvFile[:-14]
    csvFileList.append(csvBaseName)

csvFileList =  list(set(csvFileList)) 
  
wavFileList = []
for wavFile in wavFiles:
    wavBaseName = wavFile[:-4]
    wavFileList.append(wavBaseName)

wavWOcsv = []
for wav in wavFileList:
    if wav not in csvFileList:
        wavWOcsv.append(wav)

print wavWOcsv

dirExtention = "C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\Amalgamated_Files_24kHz\\"
fileList = os.listdir(dirExtention)

wav2FileList = []
for wav2 in fileList:
	wav2BaseName = wav2[:-4]
	wav2FileList.append(wav2BaseName)

fileListBlankFiles = [x for x in wav2FileList if x in wavWOcsv]

print fileListBlankFiles

randomNumbers = random.sample(xrange(len(fileListBlankFiles)), 2)
fileSelection = [fileListBlankFiles[i] for i in randomNumbers]

print fileSelection

for i in fileSelection:
    shutil.copy(dirExtention + i + '.wav', "C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\humanLabelTest\\soundFiles")


