import csv
import numpy as np
import os
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

def labelSizeBelow12kHzThreshold(df):
	maxF = row[12]
	minF = row[11]
	x1 = row[5]
	x2 = row[7]
	y1 = row[6]
	y2 = row[8]

	for row in df:
		if maxF < 12000:
			labelSize = (x2 - x1) * (y2 - y1)
		elif maxF > 12000 and minF < 12000:
			wholeLabel = (x2 - x1) * (y2 - y1)
			


def sumLabelSizes(labelList, wavfileList, wavWOcsv, csvfileDirectory):

	results = []
	zerosList = [0] * len(labelList)

	for wavFile in wavfileList:
	    row = []
	    if wavFile[:-4] in wavWOcsv:
	        row.append([wavFile] + zerosList)
	        row = list(itertools.chain(*row))
	        results.append(row)
	    else:
	        filePath = csvfileDirectory + '/' + wavFile[:-4] + '-sceneRect.csv'
	        df = read_csv(filePath)
	        row.append(wavFile)
	        for label in labelList:
	            if df.shape[0] == 1:
	                row.append('0')
	            else:
	            	### additional if statement should go here to condition the frequency of boxes to add
	                ### maybe have a function which calculates the size of boxes that overlap the frequency threshold
	                ### and then append vales to label_subset
	                label_subset = df[df['Label'] == label]
	                row.append(str(label_subset.sum()['LabelArea_DataPoints']))
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

def calculateLabelAmounts(csvfileDirectory, wavfileDirectory, resultsFileDirectory, resultsFileName):
	csvfileList, labelList = getLabelList(csvfileDirectory)
	wavWOcsv, wavfileList = getWavWOLabels(wavfileDirectory, csvfileList)
	results = sumLabelSizes(labelList, wavfileList, wavWOcsv, csvfileDirectory)
	writeResultsToCSV(resultsFileDirectory, resultsFileName, labelList, results)

# Code to implement functions

# csv441kHz = "C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/44100HzSR/csvFiles/Transport"
# wav441kHz = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/44100HzSR/wavFiles'

# csv24kHz = "C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/24000HzSR/csvFiles/Transport"
# wav24kHz = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/24000HzSR/wavFiles'

# csvRM143YB = "C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/RM14_3YB_Label_Elements"
# wavRM143YB = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/RM14_3YB_SM2+'

csvSM2BAT = "C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/Labels_SM2BAT+"
wavSM2BAT = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/SM2BAT+'

resultsFolder = "C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Results/25_Files/LabelAmounts"
resultsName = "SM2BAT_LabelAmounts"

calculateLabelAmounts(csvSM2BAT, wavSM2BAT, resultsFolder, resultsName)
