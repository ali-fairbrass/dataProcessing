import os

folderA = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\fullDataSet\\CityNetTrainData\\fromMichael\\large_audio_dataset\\large_audio_dataset\\raw_annots"
folderB = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter3 Classifier Evaluation\\fullDataSet\\CityNetTrainData\\trainingSites\\raw_annots"

listA = os.listdir(folderA)
listB = os.listdir(folderB)

listAA = []
for i in listA:
	listAA.append(i[:-14])

listBB = []
for i in listB:
	listBB.append(i[:-4])



for i in listAA:
	if i not in listBB:
		print i + ' is not a duplicate'
	else:
		pass

