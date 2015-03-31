import os

ip_dir = 'C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\2013RandomUltra\\Amalgamated_Files_192kHz'  # input folder containing audio files
op_dir = 'C:\\Users\\ucfaalf\\Documents\\Projects\\Chapter2\\2013RandomUltra\\Amalgamated_Files_192SR_12HPF'  # destination   

audio_files = os.listdir(ip_dir)  # assumes only audio files in this directory

if not os.path.isdir(op_dir):
    os.mkdir(op_dir)

for file_name in audio_files:
    print file_name
    os.system('sox ' + ip_dir + '\\' + file_name + ' ' + op_dir + '\\' + file_name + ' sinc 12k')