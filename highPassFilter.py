import os

ip_dir = 'X:/Fieldwork_Data/2015/Random_25/SM2BAT+_cropped/'  # input folder containing audio files
op_dir = 'X:/Fieldwork_Data/2015/Random_25/SM2BAT+_cropped_HPF12/'  # destination   


def highPassFilter(inputdirectory, outputdirectory):

	audio_files = os.listdir(inputdirectory)  # assumes only audio files in this directory

	if not os.path.isdir(outputdirectory):
	    os.mkdir(outputdirectory)

	for file_name in audio_files:
	    print file_name
	    os.system('sox ' + inputdirectory + '\\' + file_name + ' ' + outputdirectory + '\\' + file_name + ' sinc 12k') # Change to the desired min frequency.

highPassFilter("C:/Users/ucfaalf/Documents/Projects/AcousticAnalysis/testSM2BAT+_cropped",
	 "C:/Users/ucfaalf/Documents/Projects/AcousticAnalysis/testSM2BAT+_cropped_HPF12")