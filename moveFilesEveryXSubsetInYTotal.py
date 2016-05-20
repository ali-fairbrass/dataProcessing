import os
import shutil

wav_dir = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\extra40Recordings'
move_dir = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\infrasonicDiversityTest\\removed15Recordings'

filelist = os.listdir(wav_dir)

totalSubset = 40
filesToKeep = 25

for i in xrange(1, len(filelist), totalSubset):
    iFirstFileToRemove = i + (filesToKeep - 1)
    iFinalFileToRemove = i + (totalSubset - 1)
    iFilesToRemove = list(xrange(iFirstFileToRemove, iFinalFileToRemove))
        
    filesToRemove = [filelist[i] for i in iFilesToRemove]


    for file_name in filesToRemove:
        print '\n', "Moving: ", file_name
        shutil.move(wav_dir + '\\' + file_name, move_dir + '\\' + file_name) 
