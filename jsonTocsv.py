#This code loops through multiple .json files in a folder and writes each label within the .json file to a .csv file.
#Details of each label is parsed to a seperate row in the .csv file. Each row includes: Site code, equipment code, date, time, label,
#start and end time of label, min and max frequency of label, max, min, mean and SD amplitude of label, and label area (in datapoints on spectrogram).
#The functions to generate spectrograms (SpecGen) and to calculate label coordinates from data in the .json files (getCoordinates) are also included.
#At the moment the code can only be run on a folder containing files of the same sampling rate. The sample rate and number of rows in the spectrogram must be manually defined in lines 15 and 16.
#The filepath for the .json files, wav files, and desires location of .csv files must be defined in lines 91-93.

import json
import csv
import os
import scipy.io.wavfile
import numpy as np

#For SR44100 SpecRows=660, SR24000 SpecRows=360
SampleRate = 24000
SpecRows = 360

def SpecGen(filepath):
    """
    Function to generate a spectrogram.

    """
    sr,x = scipy.io.wavfile.read(filepath)

    ## Parameters: 10ms step, 30ms window
    nstep = int(sr * 0.01)
    nwin  = int(sr * 0.03)
    nfft = nwin

    window = np.hamming(nwin)

    ## will take windows x[n1:n2].  generate
    ## and loop over n2 such that all frames
    ## fit within the waveform
    nn = range(nwin, len(x), nstep)

    X = np.zeros( (len(nn), nfft/2) )

    for i,n in enumerate(nn):
        xseg = x[n-nwin:n]
        z = np.fft.fft(window * xseg, nfft)
        X[i,:] = np.log(np.abs(z[:nfft/2]))

    return X


def getBoxCoordinates(item, SpecRows):
    """
    Function which parses coordinates of bounding boxes in .json files to x1, x2, y1, and y2 objects.

    Takes account of different methods of drawing bounding boxes, so that coordinates are correct regardless of how bounding boxes are drawn.

    Also takes account of boxes that are accidently drawn outside of the spectrogram.

    """
    if item[0][2]>0 and item[0][3]>0:
        x1 = item[0][0]
        x2 = item[0][0] + item[0][2]
        y1 = item[0][1]
        y2 = item[0][1] + item[0][3]
    elif item[0][2]<0 and item[0][3]<0:
        x1 = item[0][0] + item[0][2]
        x2 = item[0][0]
        y1 = item[0][1] + item[0][3]
        y2 = item[0][1]
    elif item[0][2]>0 and item[0][3]<0:
        x1 = item[0][0]
        x2 = item[0][0] + item[0][2]
        y1 = item[0][1] + item[0][3]
        y2 = item[0][1]
    else:
        x1 = item[0][0] + item[0][2]
        x2 = item[0][0]
        y1 = item[0][1]
        y2 = item[0][1] + item[0][3]
    if x1 < 0:
        x1 = 0
    if y1 < 0:
        y1 = 0
    if y2 > SpecRows:
        y2 = SpecRows
    #Transform y coordinates
    y1 = (y1-SpecRows)*-1
    y2 = (y2-SpecRows)*-1


    return x1, x2, y2, y1

########################################################## JSON to CSV ########################################################################

JSON_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\24000HzSR\\jsonFiles\\AliLabels_Elements\\'
WAV_DIR = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\24000HzSR\\wavFiles\\'
csv_file = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Acoustic analysis\\Sound_Files\\25_Files\\Data\\Ali\\24000Hz_Label_Elements.csv"
filesInFolder = os.listdir(JSON_DIR)
resultFile = open(csv_file,'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerow(["SiteCode-EquipmentCode"]+["Date"]+["RecordingStartTime"]+["Label"]+["LabelStartTime_Seconds"]+["LabelEndTime_Seconds"]+["MinimumFreq_Hz"]+["MaxFreq_Hz"]+["MaxAmp"]+["MinAmp"]+["MeanAmp"]+["AmpSD"]+["LabelArea_DataPoints"])

#Define data
for jsonFile in filesInFolder:
    filePath = JSON_DIR + jsonFile
    f = open(filePath)
    data = json.load(f)
    siteCodeEquip = [jsonFile[:-29]]
    recordDate = jsonFile[-28:-20]
    recordDateEdit = [recordDate[-2:] + "/" + recordDate[-4:-2] + "/" + recordDate[:4]]
    recordTime = jsonFile[-19:-15]
    recordTimeEdit = [recordTime[:2] + ":" + recordTime[-2:] + ":00"]
    f.close()

#Generate spectrogram array
    wavFilename = jsonFile[:-15]
    wavFilepath = WAV_DIR + wavFilename + ".wav"
    X = SpecGen(wavFilepath)

# Write label data to csv file
    for item in data:
        if item[0][2] == 0 or item[0][3] == 0:
            wr.writerow(siteCodeEquip + recordDateEdit + recordTimeEdit + [item[1]]+["Not a box"])
        else:
            boxLabel = [item[1]]
            x1, x2, y1, y2 = getBoxCoordinates(item, SpecRows)
            boundingBox = X[x1:x2, y1:y2]
            startTime = [x1/100]
            endTime = [x2/100]
            minFrequency = [(y1 * (SampleRate/SpecRows))/2]
            maxFrequency = [(y2 * (SampleRate/SpecRows))/2]
            maxAmp = [np.max(boundingBox)]
            minAmp = [np.min(boundingBox)]
            meanAmp = [np.mean(boundingBox)]
            sdAmp = [np.std(boundingBox)]
            labelArea = [(x2-x1)*(y2-y1)]
            wr.writerow(siteCodeEquip + recordDateEdit + recordTimeEdit + boxLabel + startTime + endTime + minFrequency + maxFrequency + maxAmp + minAmp + meanAmp + sdAmp + labelArea)

resultFile.close()
