import os
import glob
import shutil
import random

first25FileSelection = os.listdir("Y:\\Fieldwork_Data\\2015\\Random_25\\SM2+_downSample")
out_dir = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\extra40Recordings_origSR"
# extra35from6 = os.listdir("C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 4\\infrasonicDiversityData\\extra40Recordings")
# first60FileSelection = first25FileSelection + extra35from6

data_dir = "Y:\\Fieldwork_Data\\2015"

moreSites = os.listdir(data_dir)
moreSites.remove('Random_25')

for site in moreSites:
	dirExtention = data_dir + "\\" + site + "\\SM2+_Sliced"
	fileList = os.listdir(dirExtention)
	fileListMinusFirst25 = [x for x in fileList if x not in first25FileSelection]

	randomNumbers = random.sample(xrange(len(fileListMinusFirst25)), 40)
	fileSelection = [fileList[i] for i in randomNumbers]

	for i in fileSelection:
		print "Copying " + str(i)
		shutil.copy(dirExtention + "\\" + i, out_dir)

