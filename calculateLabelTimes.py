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

	allWavfileList = os.listdir(wavfileDirectory) 

	csvfileListBase = []
	for csvFile in csvfileList:
	    csvBaseName = csvFile[:-14]
	    csvfileListBase.append(csvBaseName)
	    
	wavFileListBase = []
	for wavFile in allWavfileList:
	    wavBaseName = wavFile[:-4]
	    wavFileListBase.append(wavBaseName)

	wavWOcsv = []
	wavfileList = []
	for wav in wavFileListBase:
	    if wav not in csvfileListBase:
	        wavWOcsv.append(wav)
	    else:
	    	wavfileList.append(wav)

	return wavWOcsv, wavfileList, allWavfileList

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
    totalTimeWithSound = len(lst)*0.01
    return totalTimeWithSound



def sumLabelTimes(labelList, allWavfileList, wavWOcsv, csvfileDirectory):

	results = []
	zerosList = [0] * len(labelList)

	for wavFile in allWavfileList:
	    row = []
	    if wavFile[:-4] in wavWOcsv:
	        row.append([wavFile] + zerosList)
	        row = list(itertools.chain(*row))
	        results.append(row)
	        print wavFile + ' is in wavWOcsv'
	    else:
	    	print wavFile + ' is not in wavWOcsv'
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
			
			# totalTimeForSoundGroup = getTimeForSoundGroup(df, soundGroupList) # Figure out what is wrong with this indenting
			# print wavFile, totalTimeForSoundGroup
			# row.append(totalTimeForSoundGroup)
			# print row
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
	wavWOcsv, wavfileList, allWavfileList = getWavWOLabels(wavfileDirectory, csvfileList)
	results = sumLabelTimes(labelList, allWavfileList, wavWOcsv, csvfileDirectory)
	writeResultsToCSV(resultsFileDirectory, resultsFileName, labelList, results)

csvFolder = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\fullDataSet\\CityNetTrainData\\trainingSites\\raw_annots"
wavFolder = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\fullDataSet\\CityNetTrainData\\trainingSites\\wavs'

resultsFolder = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\FairbrassFirmanetal_\\WorkingFile\\Figures\\TableSx"
resultsName = "cityNetTrain_LabelTimes"

# soundGroupList = ["Animal", "Wing Beats", "Insect", "Bird"]
# soundGroupName = ["Biotic"]



calculateLabelTimes(csvFolder, wavFolder, resultsFolder, resultsName)

