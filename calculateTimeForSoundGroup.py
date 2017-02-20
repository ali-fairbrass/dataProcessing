import csv
import numpy as np
import os
import pandas as pd
from pandas import read_csv
import itertools

def getCSVFileList(csvfileDirectory):
	csvfileList = os.listdir(csvfileDirectory) 
	return csvfileList

def getWavWOLabels(wavfileDirectory, csvfileList):

	wavfileList = os.listdir(wavfileDirectory) 

	csvfileListBase = []
	for csvFile in csvfileList:
	    csvBaseName = csvFile[:-14]
	    csvfileListBase.append(csvBaseName)
	    
	wavFileListBase = []
	for wavFile in wavfileList:
	    wavBaseName = wavFile[:-4]
	    wavFileListBase.append(wavBaseName)

	wavWOcsv = []
	for wav in wavFileListBase:
	    if wav not in csvfileListBase:
	        wavWOcsv.append(wav)

	return wavWOcsv, wavfileList

def getSecondsWithSound(label_subset):
    
    allSecondsList = []

    for row in xrange(0, len(label_subset.index), 1):
        startTime = label_subset['LabelStartTime_Seconds'].iloc[row]
        endTime = label_subset['LabelEndTime_Seconds'].iloc[row]
        secondsList = np.arange(startTime,endTime,0.01).tolist()
        allSecondsList.append(secondsList)
    return allSecondsList

def getTimeForSoundGroup(df, soundGroupList):

    allGroupSeconds = []

    for sound in soundGroupList:
        label_subset = df[df['Label'] == sound]
        if label_subset.shape[0] != 0:
            soundSecondsList = getSecondsWithSound(label_subset)
            allGroupSeconds.append(soundSecondsList)
        else:
            pass

    merged = list(itertools.chain(*allGroupSeconds))
    merged = list(itertools.chain(*merged))
    myFormattedList = [ '%.2f' % elem for elem in merged ]
    lst = list(set(myFormattedList))
    totalTimeForSoundGroup = ("%.2f" % (len(lst)*0.01))

    return totalTimeForSoundGroup

def createResults(wavfileList, wavWOcsv, csvfileDirectory):

	results = []

	for wavFile in wavfileList:
	    row = []
	    if wavFile[:-4] in wavWOcsv:
	        row.append([wavFile] + [str(0.00)])
	        row = list(itertools.chain(*row))
	        results.append(row)
	    else:
	        filePath = csvfileDirectory + '/' + wavFile[:-4] + '-sceneRect.csv'
	        df = read_csv(filePath)
	        row.append(wavFile)
	        totalTimeForSoundGroup = getTimeForSoundGroup(df, soundGroupList)
	        row.append(totalTimeForSoundGroup)
    		results.append(row)
	return results

def writeResultsToCSV(resultsFileDirectory, resultsFileName, soundGroupName, results):
	outputFile = open(resultsFileDirectory + "\\" + resultsFileName + ".csv", "w")
	writer = csv.writer(outputFile, delimiter=',')
	columnHeader = ["Site"] + soundGroupName
	writer.writerow(columnHeader)
	writer.writerows(results)
	outputFile.close()

# soundGroupList = ["Animal", "Wing Beats", "Insect", "Bird"]
# soundGroupName = ["Biotic"]

# soundGroupList = ["Braking Vehicle (Road or Rail)", "Vehicle Alarm", "Siren", "Anthropogenic Unknown", "Metal", "Electrical Disturbance", "Human Voices", "Road Traffic", "Vehicle Horn (Road or Rail)",
# "Mechanical", "Air Traffic"]
# soundGroupName = ["Anthropogenic"]

soundGroupList = ["Rain", "Wind"]
soundGroupName = ["Abiotic"]

csvFolder = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\goldenTestSet\\40LabelFiles\\Golden"
wavFolder = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\goldenTestSet\\40WavFiles'

resultsFolder = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\goldenTestSet\\labelTimes"
resultsName = "golden_AbioticLabelTimes"

csvfileList = getCSVFileList(csvFolder)
wavWOcsv, wavfileList = getWavWOLabels(wavFolder, csvfileList)
results = createResults(wavfileList, wavWOcsv, csvFolder)
writeResultsToCSV(resultsFolder, resultsName, soundGroupName, results)