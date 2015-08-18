import os
import glob
import shutil
import random
import pandas as pd
import numpy as np
from scipy.io import wavfile


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


def cropAudioByTime(inputdirectory, outputdirectory):


    if not os.path.exists(outputdirectory):
        os.mkdir(outputdirectory)

    start_time = 0.0 # seconds    
    crop_duration = 2.0  # seconds

    audio_files = glob.glob(inputdirectory + "\\" + '*.wav')

    for ii, file_name_full in enumerate(audio_files):

        file_name = os.path.basename(file_name_full)
        #df_loc = df[df['Filename'] == file_name]
        sampling_rate, x_full = wavfile.read(file_name_full)
        file_duration = x_full.shape[0] / float(sampling_rate)

        print '\n', "Cropping file: ", os.path.basename(file_name), "of length: ", file_duration, "seconds"

        # crop
        x_crop = x_full[sampling_rate*start_time:sampling_rate*(start_time+crop_duration)]

        # save
        op_file_name = outputdirectory + "\\" + file_name[:-4] + '.wav'
        wavfile.write(op_file_name, sampling_rate, x_crop)


def highPassFilter(inputdirectory, outputdirectory):

    audio_files = os.listdir(inputdirectory)  # assumes only audio files in this directory

    if not os.path.isdir(outputdirectory):
        os.mkdir(outputdirectory)

    for file_name in audio_files:
        print '\n', "Applying high pass filter: ", file_name
        os.system('sox ' + inputdirectory + '\\' + file_name + ' ' + outputdirectory + '\\' + file_name + ' sinc 12k')

def moveFiles(inputdirectory, outputdirectory):
    
    filesToMove = os.listdir(inputdirectory)

    for fileToMove in filesToMove:

        print '\n', "Moving file: ", os.path.basename(fileToMove), "from: ", inputdirectory, "to:", outputdirectory

        os.system('move ' + '"' + inputdirectory + "\\" + fileToMove + '" "' + outputdirectory + "\\" + fileToMove + '"')


def processSM2BAT(allSM2BATFilesDirectory, randomSelectionDirectory, cropFilesDirectory, finalDirectory):
    copyRandomFiles(allSM2BATFilesDirectory, randomSelectionDirectory)
    cropAudioByTime(randomSelectionDirectory, cropFilesDirectory)
    highPassFilter(cropFilesDirectory, finalDirectory)

def moveTempFiletoFinalDirectory(tempRandomSelectionDirectory, finalRandomSelectionDirectory, tempCropFilesDirectory, finalCropFilesDirectory):
    moveFiles(tempRandomSelectionDirectory, finalRandomSelectionDirectory)
    moveFiles(tempCropFilesDirectory, finalCropFilesDirectory)

allSM2BATFilesDirectory = "Z:\\KateJonesgroup\\Ali\\Fieldwork_Data\\2015\\BR20EG\\SM2BAT+"
tempRandomSelectionDirectory = "X:\\Fieldwork_Data\\2015\\Random_25\\temp_SM2BAT+"
finalRandomSelectionDirectory = "X:\\Fieldwork_Data\\2015\\Random_25\\SM2BAT+"
tempCropFilesDirectory = "X:\\Fieldwork_Data\\2015\\Random_25\\temp_SM2BAT+_cropped"
finalCropFilesDirectory = "X:\\Fieldwork_Data\\2015\\Random_25\\SM2BAT+_cropped"
finalDirectory = "X:\\Fieldwork_Data\\2015\\Random_25\\final_SM2BAT+_test"


processSM2BAT(allSM2BATFilesDirectory, tempRandomSelectionDirectory, cropFilesDirectory, finalDirectory)

moveTempFiletoFinalDirectory(tempRandomSelectionDirectory, finalRandomSelectionDirectory, tempCropFilesDirectory, finalCropFilesDirectory)