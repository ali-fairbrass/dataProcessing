import os

"""

This deletes files from FolderB that are duplicated in FolderA.

"""

FolderA = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\goldenTestSet\\40WavFiles"
FolderB = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\fullDataSet\\CityNetTrainData\\large_audio_dataset\\large_audio_dataset\\wavs"

filesToDelete = os.listdir(FolderA)

for fileToDelete in filesToDelete:
	print 'Deleting: ' + fileToDelete
	os.remove(FolderB + '\\' + fileToDelete)