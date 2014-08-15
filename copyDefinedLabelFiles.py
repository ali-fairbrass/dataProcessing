import csv
import os
import json

JSON_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\Labels_Elements\\'
WAV_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\Amalgamated_Files\\'
jsonFiles = os.listdir(JSON_DIR)
wavFiles = os.listdir(WAV_DIR)

#Open csv results file
csv_file = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\Data\\Ali\\WavFilesBirdLabels.csv"
resultFile = open(csv_file,'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerow(["SiteCode-EquipmentCode"]+["Date"]+["RecordingStartTime"])

jsonFileList = []
for jsonFile in jsonFiles:
    filePath = JSON_DIR + jsonFile
    f = open(filePath)
    data = json.load(f)
    f.close()

    for label in data:
    	if label[1] == 'bird':
            jsonFileList.append(jsonFile)

jsonFileListNoDuplicates = list(set(jsonFileList))

jsonBaseList = []            
for fileName in jsonFileListNoDuplicates:
    jsonBaseName = fileName[:-15]
    jsonBaseList.append(jsonBaseName)
    
wavFileList = []
for wavFile in wavFiles:
    wavBaseName = wavFile[:-4]
    wavFileList.append(wavBaseName)
    
#Find wav files with no associated json file
for wav in wavFileList:
    if wav in jsonBaseList:
        siteCodeEquip = [wav[:-14]]
        recordDate = wav[-13:-5]
        recordDateEdit = [recordDate[-2:] + "/" + recordDate[-4:-2] + "/" + recordDate[:4]]
        recordTime = wav[-4:]
        recordTimeEdit = [recordTime[:2] + ":" + recordTime[-2:] + ":00"]
        wr.writerow(siteCodeEquip + recordDateEdit + recordTimeEdit)
        
resultFile.close() 