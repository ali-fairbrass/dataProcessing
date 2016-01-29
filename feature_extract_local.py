
# coding: utf-8

import os

import numpy as np

import scipy.io.wavfile as wav

from StringIO import StringIO
import urllib2

from pprint import pprint

import glob

from features import mfcc
from features import logfbank


## settings
CLASSES         = ["bird", "nobird", ]
NCLASSES        = len(CLASSES)
NMFCCS          = 13 # number of MFCCs.


ACCOUNT_NAME = 'sounds'
ACCOUNT_KEY  = 'WUfw28mwZMLHPJTH9J5ebkekMnPk6i6DyHN/5IoseyAaJE7yXu5V6FqG/nXw3sdCvEp4oo4oEYmj4Dptw0pefw==' # primary access key
HOST_BASE    = '.blob.core.windows.net'



def savedata(filename, obj):
    np.savetxt(filename, obj, delimiter=",", fmt="%s", comments = '',
               header= ",".join(["label"] +
                                ["mean%d" % x for x in range(NMFCCS)] +
                                ["var%d"  % x for x in range(NMFCCS)] ))
    
    
        
def extract_one(soundfile):

    (rate,signal) = wav.read(soundfile)
    mfcc_feat = mfcc(signal, rate, numcep=NMFCCS, preemph=0, ceplifter=0)

    mean = np.mean(mfcc_feat, axis=0)
    std  = np.std(mfcc_feat, axis=0)
    return mean, std

    
    

def extract(soundfiles, label):
    
    
    labels = np.array([label] * len(soundfiles))[np.newaxis].T
    feature_dtype = [("label", 'S6')] +                    [("mean%d" % x, 'f8') for x in range(NMFCCS)] +                    [("var%d" % x, 'f8') for x in range(NMFCCS)] 
    #X = np.ndarray( (len(soundfiles)), dtype=feature_dtype)
    X = np.zeros( (len(soundfiles), NMFCCS*2) )
    #X.label = labels
    
    counter = 0
    
    for soundfile in soundfiles:
        
        mean, std = extract_one(soundfile)
        
        # print "mean shape:", mean.shape, "std shape:", std.shape
        
        X[counter,:NMFCCS] = mean
        X[counter,NMFCCS:] = std
        
        
        counter += 1
        
    print "extracted."

    Y = np.hstack( (labels, X) )
    
    print "saving to %s.csv" % label
    savedata("%s.csv" % label , Y ) 

    
    print "saved to training and test files"
    
    return Y


# The script MUST contain a function named azureml_main
# which is the entry point for this module.
#
# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1 = None, dataframe2 = None):

    SOUND_PATHS = [
        '/Users/timosp/Documents/Magic Briefcase/current stuff/DATA AND INFO/events attended/bioacoustics warwick/birdwavs',
        '/Users/timosp/Documents/Magic Briefcase/current stuff/DATA AND INFO/events attended/bioacoustics warwick/noisewavs'
    ]

    for sound_path, label in zip(SOUND_PATHS, ["bird", "nobird"]):
        files = glob.glob(os.path.join(sound_path, "*.wav"))
    
        Y = extract(files, label)
        
        import pandas as pd
        y_train = pd.DataFrame(Y[::2] ) # every even row in X
        y_test  = pd.DataFrame(Y[1::2] ) # every even row in X
    
    
        # If a zip file is connected to the third input port is connected,
        # it is unzipped under ".\Script Bundle". This directory is added
        # to sys.path. Therefore, if your zip file contains a Python file
        # mymodule.py you can import it using:
        # import mymodule
        
        # Return value must be of a sequence of pandas.DataFrame
        # return y_train, y_test


if __name__ == '__main__':
    azureml_main()


