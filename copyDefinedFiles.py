### Copy defined files from multiple folders

import shutil
import os
from glob import glob

# Files to copy

import pandas as pd
df = pd.read_csv('Y:\\Ali\\pilotData\\recordingCheck.csv', delimiter=',')
my_files = df['recording'].tolist()
recordings = []

for i in my_files:
	filename = i + '.WAV'
	recordings.append(filename)

#  Copy files from different folders

# Function to get list of only the child directories in a folder from https://stackoverflow.com/questions/800197/how-to-get-all-of-the-immediate-subdirectories-in-python

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

dirExtention = "Y:\\Ali\\pilotData"
folderList = get_immediate_subdirectories(dirExtention)

for folder in folderList:
	filelist = os.listdir(dirExtention + '\\' + folder)

	for recording in recordings:
		if recording in filelist:
			print 'Copying: ' + recording + ' from ' + folder
			shutil.copy(dirExtention + '\\' + folder + '\\' + recording, dirExtention + '\\recordingCheck')