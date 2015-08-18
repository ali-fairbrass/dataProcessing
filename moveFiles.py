import os

ip_dir = 'Z:\\KateJonesgroup\\Ali\\Fieldwork_Data\\2014\\GreenRoofs\\'  # input folder containing files
op_dir = 'X:\\Fieldwork_Data\\2014\\GreenRoof\\'

folders = os.listdir(ip_dir)  # assumes only audio files in this directory

for folder in folders:
	subfolders = os.listdir()
    op_folder = op_dir + folder

    if not os.path.exists(op_folder):
        os.makedirs(op_folder)

    os.system('robocopy ' + '"' + ip_dir + folder + '" "' + op_dir + folder + '"')