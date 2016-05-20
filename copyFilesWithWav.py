import os
import csv
import shutil


CSV_DIR = 'C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\extra40BioticLabels'
WAV_DIR = 'C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\removed15Recordings'
csvFiles = os.listdir(CSV_DIR)
wavFiles = os.listdir(WAV_DIR)
    
csvFileList = []
for wavFile in wavFiles:
    wavBaseName = wavFile[:-4]
    csvName = wavBaseName + '-sceneRect.csv'
    csvFileList.append(csvName)

for i in csvFiles:
	if i in csvFileList:
	    print "Moving file: " + i
	    shutil.move(CSV_DIR + '\\' + i, "C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\removed15Labels")

	else:
		pass
