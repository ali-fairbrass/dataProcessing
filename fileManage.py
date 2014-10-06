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

def moveFileTypes(currentdirectory, newdirectory, fileType):
    """
    Function to move files with a defined extension to a new location.

    fileType must be defined in the format ".xxx", for example ".csv" or ".json". 
    """
    import glob
    import shutil

    dirExtention = currentdirectory + "/*" + fileType
    fileList = glob.glob(dirExtention)

    for i in fileList:
        shutil.move(i, newdirectory)
    
# moveFileTypes("C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/44100HzSR/jsonFiles/AliLabels_Elements",
#     "C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/44100HzSR/csvFiles", ".csv")