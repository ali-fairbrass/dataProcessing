import os
import csv

# Create seperate csv file per site

csv_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\first25BioticLabels\\nonChurch2015'
out_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\recordingSheets\\nonChurch2015'

labelFiles = os.listdir(csv_DIR)

siteList = ['CM167NP', 'DA5', 'E29RR', 'IG62XL', 'KT186AP', 'N17', 'N41ES', 'N88JD', 'NW10TA', 'NW23SH', 
'NW32BZ', 'NW33RY', 'RM154HX', 'SE64PL', 'SE154EE', 'SE232NZ', 'TN147QB', 'W1T4BQ']



for site in siteList:
	siteLabelList = []
	for labelFile in labelFiles:
		if site in labelFile:
			siteLabelList.append([labelFile])

	siteLabelList.insert(0, ['Filename']) 

	# os.mkdir(out_DIR + '\\' + site + 'recordingSheet.csv')

	with open(out_DIR + '\\' + site + '_recordingSheet.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(sorted(siteLabelList))