import os
import csv

# Create seperate csv file per site

wav_DIR = 'C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\second25BioticRecordings'
out_DIR = 'C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\recordingSheets\\additionalForAndy'

bioticFiles = os.listdir(wav_DIR)

nonChurch2014 = ['IG110FJ', 'N29BX', 'SE12RT-1', 'SE12RT-2', 'SE41SA', 'SE109EY',
'SE116DN', 'SE220SD', 'SW1E6BN', 'SW1W0QP', 'SW66DU', 'SW154JY', 'W55EQ',
'WC2N6RH']

nonChurch2015 = ['CM167NP', 'DA5', 'E29RR', 'IG62XL', 'KT186AP', 'N17', 'N41ES',
'N88JD', 'NW10TA', 'NW23SH', 'NW32BZ', 'NW33RY', 'RM154HX', 'SE64PL', 'SE154EE',
'SE232NZ', 'TN147QB', 'W1T4BQ']

andyFiles = ['IG110FJ', 'N29BX', 'SE12RT-1', 'SE12RT-2', 'SE41SA']

siteList = andyFiles

for site in siteList:
	siteBioticList = []
	for bioticFile in bioticFiles:
		if site in bioticFile:
			siteBioticList.append([bioticFile])

	siteBioticList.insert(0, ['Filename']) 

	# os.mkdir(out_DIR + '\\' + site + 'recordingSheet.csv')

	with open(out_DIR + '\\' + site + '_recordingSheet_secondHalf.xls', 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(siteBioticList)