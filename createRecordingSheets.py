import os
import csv

# # Create seperate csv file per site

# wav_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\second25BioticRecordings'
# out_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\recordingSheets\\churchAll'

# bioticFiles = os.listdir(wav_DIR)

# nonChurch2014 = ['IG110FJ', 'N29BX', 'SE12RT-1', 'SE12RT-2', 'SE41SA', 'SE109EY',
# 'SE116DN', 'SE220SD', 'SW1E6BN', 'SW1W0QP', 'SW66DU', 'SW154JY', 'W55EQ',
# 'WC2N6RH']

# nonChurch2015 = ['CM167NP', 'DA5', 'E29RR', 'IG62XL', 'KT186AP', 'N17', 'N41ES',
# 'N88JD', 'NW10TA', 'NW23SH', 'NW32BZ', 'NW33RY', 'RM154HX', 'SE64PL', 'SE154EE',
# 'SE232NZ', 'TN147QB', 'W1T4BQ']

# churchSites2013 = ['W112NN', 'SW154LA', 'NW1-', 'WC2H8LG', 'HA53AA', 'SE23-', 'SE3', 'CR05EF', 'E47EN']
# churchSites2014 = ['CR01SG', 'CR0-', 'RM25EL', 'RM41LD', 'TW76BE', 'W42PH', 'SE6-', 'SE84EA', 'E10NR', 'E140EY']
# churchSites2015 = ['TW76ER', 'BR20EG', 'BR28LB', 'BR67US', 'BR4', 'RM41PL']

# testSix = ['RM143YB', 'CR8', 'E105JP', 'HA86RB', 'SW112PN', 'W84LA']

# siteList = churchSites2013 + churchSites2014 + churchSites2015

# for site in siteList:
# 	siteBioticList = []
# 	for bioticFile in bioticFiles:
# 		if site in bioticFile:
# 			siteBioticList.append([bioticFile])

# 	siteBioticList.insert(0, ['Filename']) 

# 	# os.mkdir(out_DIR + '\\' + site + 'recordingSheet.csv')

# 	with open(out_DIR + '\\' + site + '_recordingSheet_secondHalf.csv', 'wb') as f:
# 		writer = csv.writer(f)
# 		writer.writerows(siteBioticList)

# To make a single recording file

wav_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4 Urban Soundscape\\infrasonicDiversityTest\\recordings_May2017'

bioticFiles = os.listdir(wav_DIR)
bioticFileList = []
for bioticFile in bioticFiles:
	bioticFileList.append([bioticFile])

bioticFileList.insert(0, ['Filename']) 

with open(wav_DIR + '\\recordingSheet_May2017.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(bioticFileList)

