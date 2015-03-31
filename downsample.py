import os

ip_dir = 'C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\2013Random\\Amalgamated_Files_MixedSR'  # input folder containing audio files
op_dir = 'C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\2013Random\\Amalgamated_Files_24kHz'  # destination   

audio_files = os.listdir(ip_dir)  # assumes only audio files in this directory

if not os.path.isdir(op_dir):
    os.mkdir(op_dir)

for file_name in audio_files:
    print file_name
    os.system('sox ' + ip_dir + '\\' + file_name  + ' -r 24k ' + op_dir + '\\' + file_name)