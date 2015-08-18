import os
import glob
import shutil
import random


#Function to copy random selection of .wav files into alternative directory (not currently working)
def copyRandomFiles(inputdirectory, outputdirectory):
    
    """
    Function to copy a random selection of 25 audio (.wav) files from one directory to another.
    
    currentdirectory is where the .wav file(s) are currently situated and must be defined in the form "C:\\...\\Folder name"
    
    newdirectory is where it is desired the .wav file(s) will be copied to. It can be defined in the same form as currentdirectory,
    or as "C:/.../Folder name"
    
    """
    if not os.path.exists(outputdirectory):
        os.mkdir(outputdirectory)

    dirExtention = inputdirectory + "/*.wav"
    fileList = glob.glob(dirExtention)
    
    randomNumbers = random.sample(xrange(len(fileList)), 25)
    fileSelection = [fileList[i] for i in randomNumbers]
    
    for i in fileSelection:
        print '\n', "Randomly selecting file: ", os.path.basename(i)
        shutil.copy(i, outputdirectory)


def downSample(inputdirectory, outputdirectory):

    audio_files = os.listdir(inputdirectory)  # assumes only audio files in this directory

    if not os.path.isdir(outputdirectory):
        os.mkdir(outputdirectory)

    for file_name in audio_files:
        print '\n', "Downsampling: ", file_name
        os.system('sox ' + inputdirectory + '\\' + file_name  + ' -r 24k ' + outputdirectory + '\\' + file_name)


def moveFiles(inputdirectory, outputdirectory):
    
    filesToMove = os.listdir(inputdirectory)

    for fileToMove in filesToMove:

        print '\n', "Moving file: ", os.path.basename(fileToMove), "from: ", inputdirectory, "to:", outputdirectory

        os.system('move ' + '"' + inputdirectory + "\\" + fileToMove + '" "' + outputdirectory + "\\" + fileToMove + '"')


def processSM2(allSM2FilesDirectory, tempSM2FilesDirectory, downsampledM2FilesDirectory):
    copyRandomFiles(allSM2FilesDirectory, tempSM2FilesDirectory)
    downSample(tempSM2FilesDirectory, downsampledM2FilesDirectory)


def moveTempFiletoFinalDirectory(tempRandomSelectionDirectory, finalRandomSelectionDirectory):
    moveFiles(tempRandomSelectionDirectory, finalRandomSelectionDirectory)


allSM2FilesDirectory = "X:\\Fieldwork_Data\\2015\\BR20EG\\SM2+_Sliced"
tempSM2FilesDirectory = "X:\\Fieldwork_Data\\2015\\Random_25\\temp_SM2+"
downsampledM2FilesDirectory = "X:\\Fieldwork_Data\\2015\\Random_25\\test_SM2+_downsample"

# processSM2(allSM2FilesDirectory, tempSM2FilesDirectory, downsampledM2FilesDirectory)
moveTempFiletoFinalDirectory(tempSM2FilesDirectory, downsampledM2FilesDirectory)

