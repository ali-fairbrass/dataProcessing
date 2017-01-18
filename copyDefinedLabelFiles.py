import os
import csv
import shutil

CSV_DIR = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\LabelsCSV'
WAV_DIR = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\Amalgamated_Files'
OUT_DIR = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 2 Acoustic analysis\\Fairbrass_JoAE\\WorkingFile\\Figures\\FigS2\\exampleAudio"
csvFiles = os.listdir(CSV_DIR)
wavFiles = os.listdir(WAV_DIR)

bioticSounds = ['bird', 'invertebrate', 'animal', 'wing beats', 'bat', 'Squirrel', 'fox', 'insect', 'grey squirrel', 'wingBeats', 'amphibian', 'cat']

# church2015 = ['TW76ER', 'BR20EG', 'BR28LB', 'BR67US', 'BR4', 'RM41PL']

# labelList = []
# for csvFile in csvFiles:
#     filePath = CSV_DIR + '\\' + csvFile
#     with open(filePath, 'rb') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             labelList.append(row[1])

# print list(set(labelList))

labelFileList = []
for csvFile in csvFiles:
    filePath = CSV_DIR + '\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] in bioticSounds:
                labelFileList.append(csvFile)

# print len(sorted(list(set(labelFileList))))
# labelFileListNoDuplicates = list(set(birdFileList))
# voiceFileListNoDuplicates = list(set(voiceFileList))

# birdNoVoices = []
# for i in birdFileListNoDuplicates:
#     if i not in voiceFileListNoDuplicates:
#         birdNoVoices.append(i)

csvBaseList = []
for fileName in list(set(labelFileList)):
    csvBaseName = fileName[:-14]
    csvBaseList.append(csvBaseName)
    
wavFileList = []
for wavFile in wavFiles:
    wavBaseName = wavFile[:-4]
    wavFileList.append(wavBaseName)
    
# Find wav files with defined label and copy to folder
for wav in wavFileList:
    if wav in csvBaseList:
        wavExtension = WAV_DIR + '\\' + wav + ".wav"
        shutil.copy(wavExtension, OUT_DIR)
        print "Copying file: " + wav

# #Write filenames to csv file
# with open(OUT_DIR + '\\birdFiles.csv', 'wb') as f:
#     writer = csv.writer(f)
#     writer.writerows([sorted(csvBaseList)])

# Copy label files

# for labelFile in labelFileList:
#     shutil.copy(CSV_DIR + '\\' + labelFile, OUT_DIR)
#     print "Copying file: " + labelFile