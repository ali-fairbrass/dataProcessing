import pandas as pd
import numpy as np
from scipy.io import wavfile
import os
import glob

data_dir = 'X:/Fieldwork_Data/2015/Random_25/SM2BAT+/'
op_dir = 'X:/Fieldwork_Data/2015/Random_25/SM2BAT+_cropped/'

if not os.path.exists(op_dir):
    os.mkdir(op_dir)

start_time = 0.0 # seconds    
crop_duration = 2.0  # seconds

audio_files = glob.glob(data_dir + '*.wav')

# op_info = []

for ii, file_name_full in enumerate(audio_files):

    file_name = os.path.basename(file_name_full)
    #df_loc = df[df['Filename'] == file_name]
    sampling_rate, x_full = wavfile.read(file_name_full)
    file_duration = x_full.shape[0] / float(sampling_rate)

    print '\n', os.path.basename(file_name), file_duration

    # crop
    x_crop = x_full[sampling_rate*start_time:sampling_rate*(start_time+crop_duration)]

    # save
    op_file_name = op_dir + file_name[:-4] + '.wav'
    wavfile.write(op_file_name, sampling_rate, x_crop)