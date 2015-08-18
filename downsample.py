import os

ip_dir = 'X:\\Fieldwork_Data\\2015\\Random_25\\BR28LB'  # input folder containing audio files
op_dir = 'X:\\Fieldwork_Data\\2015\\Random_25\\SM2+_downSample'  # destination   

audio_files = os.listdir(ip_dir)  # assumes only audio files in this directory

if not os.path.isdir(op_dir):
    os.mkdir(op_dir)

for file_name in audio_files:
    print file_name
    os.system('sox ' + ip_dir + '\\' + file_name  + ' -r 24k ' + op_dir + '\\' + file_name)