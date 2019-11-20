import csv
import numpy as np
import os
import pandas as pd
from pandas import read_csv
import itertools

def getLabelList(csvfileDirectory):

	Labels = []
	csvfileList = os.listdir(csvfileDirectory) 
	
	if "batdetector_results.csv" in csvfileList: 
		csvfileList.remove("batdetector_results.csv")

	for csvFile in csvfileList:
		print csvFile
		filePath = csvfileDirectory + '/' + csvFile
		with open(filePath, 'r') as resultsFile:
			resultsFile.next() # skip the header
			reader = csv.reader(resultsFile)
			for row in reader:
				Label = row[1]
				print Label
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

def labelSizeBelow12kHz(specHeight, sampleRate, csvfileDirectory, resultsFileDirectory, resultsFileName):
    
    csvfileList = os.listdir(csvfileDirectory) 
    
    yValueAt12kHz = (specHeight - (12000/((sampleRate/2)/specHeight)))
    
    for csvFile in csvfileList:
        filePath = csvfileDirectory + '\\' + csvFile
        df = read_csv(filePath)
        if df.shape[0] != 1:
            df['LabelArea_Datapoints_Threshold'] = np.where(df['MaximumFreq_Hz'] < 12000, 
                                                    ((df['Spec_x2'] - df['Spec_x1']) * (df['Spec_y2'] - df['Spec_y1'])),
                                                    ((df['Spec_x2'] - df['Spec_x1']) * (df['Spec_y2'] - yValueAt12kHz)))
            df['LabelArea_Datapoints_Threshold'][df['LabelArea_Datapoints_Threshold'] < 0] = 0
            df.to_csv(resultsFileDirectory + "\\" + csvFile[:-14] + resultsFileName + ".csv", sep=',', index=False) #use -14 for 24 and 44.1kHz and -18 for RM143YB
        else:
            pass

def labelSizeAbove12kHz(specHeight, sampleRate, csvfileDirectory, resultsFileDirectory, resultsFileName):
    
    csvfileList = os.listdir(csvfileDirectory) 
    
    yValueAt12kHz = (specHeight - (12000/((sampleRate/2)/specHeight)))
    
    for csvFile in csvfileList:
        filePath = csvfileDirectory + '\\' + csvFile
        df = read_csv(filePath)
        if df.shape[0] != 1:
            df['LabelArea_Datapoints_Threshold'] = np.where(df['MinimumFreq_Hz'] > 12000, 
                                                    ((df['Spec_x2'] - df['Spec_x1']) * (df['Spec_y2'] - df['Spec_y1'])),
                                                    ((df['Spec_x2'] - df['Spec_x1']) * (yValueAt12kHz - df['Spec_y1'])))
            df['LabelArea_Datapoints_Threshold'][df['LabelArea_Datapoints_Threshold'] < 0] = 0
            df.to_csv(resultsFileDirectory + "\\" + csvFile[:-14] + resultsFileName + ".csv", sep=',', index=False) #use -14 for 24 and 44.1kHz and -18 for RM143YB
        else:
            pass
			
def sumLabelSizes(labelList, wavfileList, wavWOcsv, csvfileDirectory):

	results = []
	zerosList = [0] * len(labelList)

	for wavFile in sorted(wavfileList):
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
	            if df.shape[0] == 1:
	                row.append('0')
	            else:
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

# To generate threshold data for SM2+

# labelSizeBelow12kHz(360, 24000, "C:\\Users\\ucfaalf\\Documents\\Projects\\Acoustic Analysis\\2013Random\\LabelsCSVTransport\\24000HzSR", 
#                            "C:\\Users\\ucfaalf\\Dropbox\\EngD\Projects\\Chapter 2 Acoustic analysis\\Data\\LabelsCSVTransportThreshold\\24000HzSR", "_below12kHz")

# labelSizeBelow12kHz(660, 44100, "C:\\Users\\ucfaalf\\Documents\\Projects\\Acoustic Analysis\\2013Random\\LabelsCSVTransport\\41000HzSR", 
#                            "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 2 Acoustic analysis\\Data\\LabelsCSVTransportThreshold\\41000HzSR", "_below12kHz")

# labelSizeBelow12kHz(2880, 192000, "C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\SoundFiles\\LabelsCSV\\192000kHz", 
#                            "C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\SoundFiles\\LabelsCSVThreshold\\192000kHz", "_below12kHz")

# To generate threshold data for SM2BAT+

# labelSizeAbove12kHz(288, 192000, "C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\2013RandomUltra\\Labels_SM2BAT+\\192kHzSR", 
#                            "C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\2013RandomUltra\\Labels_SM2BAT+_Threshold\\192kHzSR", 
#                            "_above12kHz")

# labelSizeAbove12kHz(576, 384000, "C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\2013RandomUltra\\Labels_SM2BAT+\\384kHzSR", 
#                            "C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\2013RandomUltra\\Labels_SM2BAT+_Threshold\\384kHzSR", 
#                            "_above12kHz")

# labelSizeAbove12kHz(288, 192000, "C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\2013RandomUltra\\Labels_SM2BAT+\\RM143YB", 
#                            "C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\2013RandomUltra\\Labels_SM2BAT+_Threshold\\RM143YB", 
#                            "_above12kHz")

# # To generate overall label amounts data

csvFolder = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4 Urban Soundscape\\Data\\random_SE232NZ\\label"
wavFolder = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4 Urban Soundscape\\Data\\random_SE232NZ\\2secCrop'

# # csv24kHz = "C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/24000HzSR/csvFiles/Transport"
# # wav24kHz = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/24000HzSR/wavFiles'

# # csvRM143YB = "C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/RM14_3YB_Label_Elements"
# # wavRM143YB = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/RM14_3YB_SM2+'

# # csvSM2BAT = "C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/Labels_SM2BAT+"
# # wavSM2BAT = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/SM2BAT+'

resultsFolder = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4 Urban Soundscape\\Data\\random_SE232NZ"
resultsName = "SE222NZ_labelAmounts"

calculateLabelAmounts(csvFolder, wavFolder, resultsFolder, resultsName)
