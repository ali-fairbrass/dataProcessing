import csv
import os

JSON_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\Labels_Elements\\'
WAV_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\Amalgamated_Files\\'
jsonFiles = os.listdir(JSON_DIR)
wavFiles = os.listdir(WAV_DIR)

#Open csv results file
csv_file = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\Data\\Ali\\WavFilesWithoutLabels_Test.csv"
resultFile = open(csv_file,'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerow(["SiteCode-EquipmentCode"]+["Date"]+["RecordingStartTime"])

#Remove file extensions and excess characters from filenames so that filenames in both lists are matching
jsonFileList = []
for jsonFile in jsonFiles:
    jsonBaseName = jsonFile[:-15]
    jsonFileList.append(jsonBaseName)
    
wavFileList = []
for wavFile in wavFiles:
    wavBaseName = wavFile[:-4]
    wavFileList.append(wavBaseName)
    
#Find wav files with no associated json file and print details of each wav file to new row in csv file
for wav in wavFileList:
    if wav not in jsonFileList:
        siteCodeEquip = [wav[:-14]]
        recordDate = wav[-13:-5]
        recordDateEdit = [recordDate[-2:] + "/" + recordDate[-4:-2] + "/" + recordDate[:4]]
        recordTime = wav[-4:]
        recordTimeEdit = [recordTime[:2] + ":" + recordTime[-2:] + ":00"]
        wr.writerow(siteCodeEquip + recordDateEdit + recordTimeEdit)
        
resultFile.close() 