import os

ip_dir = 'C:\\Users\\ucfaalf\\Dropbox\\mixtest\\originalData\\'  # input folder containing audio files
op_dir = 'C:\\Users\\ucfaalf\\Dropbox\\mixtest\\12secData\\'  # destination   

audio_files = os.listdir(ip_dir)

# print type(float(len(audio_files)/4))

fileNumber = 0

numberOfLongFiles = len(audio_files)/4

# for longFile in range(1,numberOfLongFiles):

for i in range(1,numberOfLongFiles):

	fileNumber = fileNumber + 1
	firstRecording = ip_dir + audio_files[fileNumber]

	fileNumber = fileNumber + 1
	secondRecording = ip_dir + audio_files[fileNumber]

	fileNumber = fileNumber + 1
	thirdRecording = ip_dir + audio_files[fileNumber]

	fileNumber = fileNumber + 1
	fourthRecording = ip_dir + audio_files[fileNumber]

	os.system('sox ' + firstRecording + ' ' + secondRecording + ' ' + thirdRecording + ' ' + fourthRecording + ' ' + op_dir + '\\' + 'longRecording_' + str(i) + '.wav') 