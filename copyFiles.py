import os

#Function to copy random selection of .wav files into alternative directory (not currently working)
def copyRandomFiles(currentdirectory, newdirectory, randomfiles):
    
    """
    Function to copy a random selection of audio (.wav) files from one directory to another.
    
    currentdirectory is where the .wav file(s) are currently situated and must be defined in the form "C:\\...\\Folder name"
    
    newdirectory is where it is desired the .wav file(s) will be copied to. It can be defined in the same form as currentdirectory,
    or as "C:/.../Folder name"
    
    randomfiles is an integer of the number of randomly selected files are desired to be moved
    
    """
    
    import glob
    import shutil
    import random
    dirExtention = currentdirectory + "/*.wav"
    fileList = glob.glob(dirExtention)
    
    randomNumbers = random.sample(xrange(len(fileList)), randomfiles)
    fileSelection = [fileList[i] for i in randomNumbers]
    
    for i in fileSelection:
        shutil.copy(i, newdirectory)

ip_dir = 'X:\\Fieldwork_Data\\2015\\BR28LB\\SM2+_Sliced'
op_dir = 'X:\\Fieldwork_Data\\2015\\Random_25\\BR28LB'

if not os.path.exists(op_dir):
        os.makedirs(op_dir)

copyRandomFiles(ip_dir, 
            op_dir, 25)