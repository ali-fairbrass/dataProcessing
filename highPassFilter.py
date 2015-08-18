import os

ip_dir = 'X:/Fieldwork_Data/2015/Random_25/SM2BAT+_cropped/'  # input folder containing audio files
op_dir = 'X:/Fieldwork_Data/2015/Random_25/SM2BAT+_cropped_HPF12/'  # destination   

audio_files = os.listdir(ip_dir)  # assumes only audio files in this directory

if not os.path.isdir(op_dir):
    os.mkdir(op_dir)

for file_name in audio_files:
    print file_name
    os.system('sox ' + ip_dir + '\\' + file_name + ' ' + op_dir + '\\' + file_name + ' sinc 12k')