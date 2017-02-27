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
	if df.shape[0] > 3:
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

	else:
		totalTimeForSoundGroup = 0

	if float(totalTimeForSoundGroup) > 60.00:
		totalTimeForSoundGroup = 60.00
	else:
		pass

	return totalTimeForSoundGroup

def createResults(wavfileList, wavWOcsv, csvfileDirectory):

	results = []

	for wavFile in wavfileList:
		print "Processing: " + str(wavFile)
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

# soundGroupList = ["Squirrel", "amphibian", "animal", "bird", "cat", "fox", "grey squirrel", 
# "insect", "invertebrate", "wing beats", "wingBeats", "wings beating"]
# soundGroupName = ["Biotic"]
# soundGroupListGolden = ["Animal", "Wing Beats", "Insect", "Bird"]

# soundGroupListGolden = ["Braking Vehicle (Road or Rail)", "Vehicle Alarm", "Siren", "Anthropogenic Unknown", "Metal", "Electrical Disturbance", "Human Voices", "Road Traffic", "Vehicle Horn (Road or Rail)",
# "Mechanical", "Air Traffic"]
# soundGroupList = ['Braking', 'Bus emitting', 'Horn', 'Mix traffic', 'StarttheCar', 'Train doors (beeping)', 'airplane', 'alarm' 'anthropogenic unknown', 
# 'applause', 'ball bouncing', 'barking dog',
# 'bat hitting ball', 'beep', 'bells', 'breaking vehicle', 'building ventilation system', 'camera', 'car alarm', 'car horn', 'cat', 
# 'church bell', 'church bells', 'clapping', 'coughing', 'deck lowering', 'dog bark', 'dog barking', 'door opening', 'electrical', 
# 'electrical disturbance', 'footsteps', 'glass into bins', 'hammering', 'horn', 'human voice', 'laughing', 'lawnmower', 'machinery', 
# 'mechanical', 'metal', 'metalic', 'metalic sound', 'mix traffic' 'mobile phone', 'mower', 'music', 'rail traffic', 'road traffic', 'rubbish bag', 'shower', 
# 'siren', 'sweeping broom', 'television', 'train horn', 'train station announcement', 'vehicle breaking', 'vehicle horn', 'voices', 'whistle']
# soundGroupName = ["Anthropogenic"]

# soundGroupListGolden = ["Rain", "Wind"]
soundGroupList = ['dripping water', 'rain', 'rainfall on vegetation', 'rock', 'russling leaves (animal)', 'russling vegetation (animal)',
'vegetation', 'water dripping', 'water splashing', 'wind']
soundGroupName = ["Abiotic"]

# #2013 data
# csvFolder = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Data\\201Random\\allLabelFiles"
# wavFolder = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\Amalgamated_Files'

# # # 2014 data
# csvFolder = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Data\\2014Random\\allLabelFiles"
# wavFolder = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2014Random\\wavFiles'

# 2015 data
csvFolder = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Data\\2015Random\\allLabelFiles"
wavFolder = 'C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2015Random\\allWavFiles'

resultsFolder = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\fullDataSet\\labelTimes\\Abiotic\\"
resultsName = "2015_abioticLabelTimes"

csvfileList = getCSVFileList(csvFolder)
wavWOcsv, wavfileList = getWavWOLabels(wavFolder, csvfileList)
results = createResults(wavfileList, wavWOcsv, csvFolder)
writeResultsToCSV(resultsFolder, resultsName, soundGroupName, results)