import os

inputdirectory = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\temp"  # input folder containing audio files
outputdirectory = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\extra40Recordings"  # destination   

def downSample(inputdirectory, outputdirectory):

	audio_files = os.listdir(inputdirectory)  # assumes only audio files in this directory

	if not os.path.isdir(outputdirectory):
	    os.mkdir(outputdirectory)

	for file_name in audio_files:
	    print '\n', "Downsampling: ", file_name
	    os.system('sox ' + inputdirectory + '\\' + file_name  + ' -r 24k ' + outputdirectory + '\\' + file_name) #Change 24k to whatever sample rate you want

downSample(inputdirectory, outputdirectory)