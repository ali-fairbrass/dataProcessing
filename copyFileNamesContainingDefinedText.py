import os
import shutil

"""
Copy files whose filename contains some defined text.
"""

folderA = "C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\allAnnotatedFirst25Files\\labelFiles"
folderB = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\fullDataSet\\CityNetTrainData\\testSites\\raw_annots"

definedText = ["W112NN", "WC2H8LG", "HA86RB", "HA53AA", "SE23", "SE3", "CR8", "CR05EF", "E105JP", "SW154JY", "IG62XL", "E29RR", "TW76ER", "BR20EG", "BR28LB", "BR67US", "BR4", "DA5", "CM167NP"]
# definedText = ["CR0", "CR01SG", "E10NR", "E140EY", "E47EN", "IG110FJ", "KT186AP", "N17", "N29BX", "N41ES", "N88JD", "NW1", "NW10TA", "NW23SH", "NW32BZ", "NW33RY", "RM143YB", 
# "RM154HX", "RM25EL", "RM41LD", "RM41PL", "SE109EY", "SE116DN", "SE12RT-1", "SE12RT-2", "SE154EE", "SE220SD", "SE232NZ", "SE41SA", "SE6", "SE64PL", "SE84EA", "SW112PN", "SW154LA",
# "SW1E6BN", "SW1W0QP", "SW66DU", "TN147QB", "TW76BE", "W1T4BQ", "W42PH", "W55EQ", "W84LA", "WC2N6RH"]

fileList = os.listdir(folderA)

filesToCopy = []

for File in fileList:
	for text in definedText:
		if text in File:
			filesToCopy.append(File)
		else:
			pass

for File in filesToCopy:
	print 'Copying file: ' + File
	shutil.copy(folderA + '\\' + File, folderB)