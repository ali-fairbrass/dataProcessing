import os
import glob
import shutil
import csv

wavFileList = []
labelFileList = []

DIR = "C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\"
labelFiles = os.listdir(DIR + "extra25BioticLabels")

for label in labelFiles:
	labelFileList.append(label[:-14])


for i in labelFileList:
	print "Copying " + str(i)
	shutil.copy(DIR + "extra25Recordings\\" + str(i) + ".wav", DIR + "second25BioticRecordings")

# #Write filenames to csv file
# with open(DIR + '\\birdFiles.csv', 'wb') as f:
#     writer = csv.writer(f)
#     writer.writerows([sorted(birdWav)])
