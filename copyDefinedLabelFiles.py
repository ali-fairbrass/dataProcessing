import os
import csv
import shutil

CSV_DIR = 'Y:\\Fieldwork_Data\\2015\\Random_25\\SM2+_VerityLabels'
WAV_DIR = 'Y:\\Fieldwork_Data\\2015\\Random_25\\SM2+_downSample\\'
OUT_DIR = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 3\\goldenTestSet\\21VerityFiles\\"
csvFiles = os.listdir(CSV_DIR)
wavFiles = os.listdir(WAV_DIR)

labelList = []
for csvFile in csvFiles:
    filePath = CSV_DIR + '\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            labelList.append(row[1])

print list(set(labelList))

# birdFileList = []
# for csvFile in csvFiles:
#     filePath = CSV_DIR + '\\' + csvFile
#     with open(filePath, 'rb') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if row[1] == 'bird':
#                 birdFileList.append(csvFile)


# birdFileListNoDuplicates = list(set(birdFileList))
# # voiceFileListNoDuplicates = list(set(voiceFileList))

# # birdNoVoices = []
# # for i in birdFileListNoDuplicates:
# #     if i not in voiceFileListNoDuplicates:
# #         birdNoVoices.append(i)

# csvBaseList = []
# for fileName in birdFileListNoDuplicates:
#     csvBaseName = fileName[:-14]
#     csvBaseList.append(csvBaseName)
    
# wavFileList = []
# for wavFile in wavFiles:
#     wavBaseName = wavFile[:-4]
#     wavFileList.append(wavBaseName)
    
# #Find wav files with defined label and copy to folder
# for wav in wavFileList:
#     if wav in csvBaseList:
#         wavExtension = WAV_DIR + '\\' + wav + ".wav"
#         shutil.copy(wavExtension, OUT_DIR)
#         print "Copying file: " + wav

# #Write filenames to csv file
# with open(OUT_DIR + '\\birdFiles.csv', 'wb') as f:
#     writer = csv.writer(f)
#     writer.writerows([sorted(csvBaseList)])