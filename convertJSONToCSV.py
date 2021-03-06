#Converting json label files to csv files
import os

json24kHzFolder = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/24000HzSR/jsonFiles/TransportLabels'
wav24kHzFolder = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/24000HzSR/wavFiles'
json441kHzFolder = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/44100HzSR/jsonFiles/TransportLabels'
wav441kHzFolder = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/44100HzSR/wavFiles'

# testJSON = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Acoustic analysis/Sound_Files/25_Files/24000HzSR/jsonFiles/AliLabels_Elements/HA53AA-13548_20130724_0452-sceneRect.json'
# testWAV = 'C:/Users/ucfaalf/Dropbox/EngD/Projects/Chapter 2 Acoustic analysis/Sound_Files/25_Files/24000HzSR/wavFiles/HA53AA-13548_20130724_0452.wav'


jsonInFolder = os.listdir(json24kHzFolder)
# wavInFolder = os.listdir(wav24kHzFolder)

for jsonFile in jsonInFolder:
	jsonFilepath = json24kHzFolder + '/' + jsonFile
	wavFilepath = wav24kHzFolder + '/' + jsonFile[:-15] + '.wav'
	convertJSON2CSV(jsonFilepath, wavFilepath)

# convertJSON2CSV(testJSON, testWAV, csvAppendix='-test')

# spec = SpecGen(testWAV)
# print spec.shape[1]


import AudioTagger.converter as C
jsonFileTest = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 2 Acoustic analysis\\Sound_Files\\25_Files\\44100HzSR\\jsonFiles\\AliLabels_Elements\\SE3-13548_20130909_0734-sceneRect.json'
wavFileTest = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 2 Acoustic analysis\\Sound_Files\\25_Files\\44100HzSR\\wavFiles\\SE3-13548_20130909_0734.wav'

C.convertJSON2CSV(jsonFileTest, wavFileTest)