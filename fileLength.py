import os

ip_dir = 'Z:\\KateJonesgroup\\Ali\\Fieldwork_Data\\2013\\HA5_3AA\\SM2BAT+'  # input folder containing audio files

audio_files = os.listdir(ip_dir)  # assumes only audio files in this directory

for file_name in audio_files:
    # print file_name
    os.system('soxi -D ' + ip_dir + '\\' + file_name)

# To write output to a text file in console use:

# python -u C:\Users\ucfaalf\Documents\GitHub\dataProcessing\fileLength.py > HA5_3AA_night.txt
