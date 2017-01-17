import csv
import numpy as np
import os
import pandas as pd
from pandas import read_csv
import itertools

def getLabelList(csvfileDirectory):

	Labels = []
	csvfileList = os.listdir(csvfileDirectory) 

	for csvFile in csvfileList:
	    filePath = csvfileDirectory + '/' + csvFile
	    with open(filePath, 'r') as resultsFile:
	        resultsFile.next() # skip the header
	        reader = csv.reader(resultsFile)
	        for row in reader:
	            Label = row[1]
	            Labels.append(Label)

	resultsFile.close()

	labelList = list(set(Labels))
	
	return csvfileList, labelList

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

def getTotalTimeWithSound(allSecondsList):
    
    merged = list(itertools.chain(*allSecondsList))
    myFormattedList = [ '%.2f' % elem for elem in merged ]
    lst = list(set(myFormattedList))
    lst1 = [float(i) for i in lst]
    maxTime = max(lst1)
    minTime = min(lst1)
    totalTimeWithSound = maxTime - minTime
    return totalTimeWithSound

def sumLabelTimes(labelList, wavfileList, wavWOcsv, csvfileDirectory):

	results = []
	zerosList = [0] * len(labelList)

	for wavFile in wavfileList:
	    row = []
	    if wavFile[:-4] in wavWOcsv:
	        row.append([wavFile] + zerosList)
	        row = list(itertools.chain(*row))
	        results.append(row)
	    else:
	        filePath = csvfileDirectory + '/' + wavFile[:-4] + '-sceneRect.csv' # Changed from "_below12kHz.csv" for SM2BAT data
	        df = read_csv(filePath)
	        row.append(wavFile)
	        for label in labelList:
	        	label_subset = df[df['Label'] == label]
	        	if label_subset.shape[0] == 0:
	        		row.append('0')
	        	else:
					allSecondsList = getSecondsWithSound(label_subset)
					totalTimeWithSound = getTotalTimeWithSound(allSecondsList)
					row.append(str(totalTimeWithSound))
	        results.append(row)

	return results

def writeResultsToCSV(resultsFileDirectory, resultsFileName, labelList, results):
	outputFile = open(resultsFileDirectory + "/" + resultsFileName + ".csv", "w")
	writer = csv.writer(outputFile, delimiter=',')
	labelList.insert(0, "Site")
	columnHeader = labelList
	writer.writerow(columnHeader)
	writer.writerows(results)
	outputFile.close()

def calculateLabelTimes(csvfileDirectory, wavfileDirectory, resultsFileDirectory, resultsFileName):
	csvfileList, labelList = getLabelList(csvfileDirectory)
	wavWOcsv, wavfileList = getWavWOLabels(wavfileDirectory, csvfileList)
	results = sumLabelTimes(labelList, wavfileList, wavWOcsv, csvfileDirectory)
	writeResultsToCSV(resultsFileDirectory, resultsFileName, labelList, results)

csvFolder = "C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\goldenTestSet\\40LabelFiles\\Ali"
wavFolder = 'C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\goldenTestSet\\40WavFiles'

resultsFolder = "C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\goldenTestSet\\labelTimes"
resultsName = "ali_LabelTimes"

calculateLabelTimes(csvFolder, wavFolder, resultsFolder, resultsName)