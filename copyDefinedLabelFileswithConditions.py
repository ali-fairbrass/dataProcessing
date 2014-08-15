import os
import json
import shutil

JSON_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\Labels_Elements\\'
WAV_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\Amalgamated_Files\\'
jsonFiles = os.listdir(JSON_DIR)
wavFiles = os.listdir(WAV_DIR)

birdFileList = []
voiceFileList = []
for jsonFile in jsonFiles:
    filePath = JSON_DIR + jsonFile
    f = open(filePath)
    data = json.load(f)
    f.close()

    for label in data:
        if label[1] == 'bird':
            birdFileList.append(jsonFile)
    
    for label in data:
        if label[1] == 'voices':
            voiceFileList.append(jsonFile)

birdFileListNoDuplicates = list(set(birdFileList))
voiceFileListNoDuplicates = list(set(voiceFileList))

birdNoVoices = []
for i in birdFileListNoDuplicates:
    if i not in voiceFileListNoDuplicates:
        birdNoVoices.append(i)

jsonBaseList = []
for fileName in birdNoVoices:
    jsonBaseName = fileName[:-15]
    jsonBaseList.append(jsonBaseName)
    
wavFileList = []
for wavFile in wavFiles:
    wavBaseName = wavFile[:-4]
    wavFileList.append(wavBaseName)
    
#Find wav files with defined label and copy to folder
for wav in wavFileList:
    if wav in jsonBaseList:
    	wavExtension = WAV_DIR + wav + ".wav"
    	shutil.copy(wavExtension, "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\BirdFiles\\FilesWithoutVoices")