import os

ip_dir = 'Y:\\Ali\\pilotData'  # input folder containing audio files
op_dir = 'F:\\pilotData\\'  # destination   

folders = range(1,16)

print(folders)

for folder in folders:
	inputdirectory = ip_dir + "\\" + str(folder)
	outputdirectory = op_dir + "\\" + str(folder)

	print("copying data from " + inputdirectory + " to " + outputdirectory)

	os.system('robocopy "' + inputdirectory + '" "' + outputdirectory)


# def highPassFilter(inputdirectory, outputdirectory):

# 	audio_files = os.listdir(inputdirectory)  # assumes only audio files in this directory

# 	if not os.path.isdir(outputdirectory):
# 	    os.mkdir(outputdirectory)

# 	for file_name in audio_files:
# 	    print file_name
# 	    os.system('sox ' + inputdirectory + '\\' + file_name + ' ' + outputdirectory + '\\' + file_name + ' sinc 12k') # Change to the desired min frequency.

# highPassFilter(ip_dir, op_dir)