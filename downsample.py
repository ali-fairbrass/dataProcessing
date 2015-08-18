import os

ip_dir = 'X:\\Fieldwork_Data\\2015\\Random_25\\BR28LB'  # input folder containing audio files
op_dir = 'X:\\Fieldwork_Data\\2015\\Random_25\\SM2+_downSample'  # destination   

def downSample(inputdirectory, outputdirectory):

	audio_files = os.listdir(inputdirectory)  # assumes only audio files in this directory

	if not os.path.isdir(outputdirectory):
	    os.mkdir(outputdirectory)

	for file_name in audio_files:
	    print '\n', "Downsampling: ", file_name
	    os.system('sox ' + inputdirectory + '\\' + file_name  + ' -r 24k ' + outputdirectory + '\\' + file_name)