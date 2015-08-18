import pandas as pd
import numpy as np
from scipy.io import wavfile
import os
import glob

# TODO set these
op_dir = 'C:/Users/omacaodh/Downloads/urban_sounds/cropped_audio/'
op_labels_file = 'C:/Users/omacaodh/Downloads/urban_sounds/cropped_label.txt'

label_file = 'C:/Users/omacaodh/Downloads/urban_sounds/urban_sounds_labels.csv'
data_dir = 'C:/Users/omacaodh/Downloads/urban_sounds/audio/'

if not os.path.exists(op_dir):
    os.mkdir(op_dir)

crop_duration = 4.0  # seconds

df = pd.read_csv(label_file)

audio_files = glob.glob(data_dir + '*.wav')
op_info = []

for ii, file_name_full in enumerate(audio_files):

    file_name = os.path.basename(file_name_full)
    df_loc = df[df['Filename'] == file_name]
    sampling_rate, x_full = wavfile.read(file_name_full)
    file_duration = x_full.shape[0] / float(sampling_rate)

    print '\n', os.path.basename(file_name), file_duration

    for jj, loc_event in enumerate(df_loc.iterrows()):
        event_time = loc_event[1]['LabelStartTime_Seconds']
        event_label = loc_event[1]['Label']

        print event_time, event_label

        # crop
        x_crop = x_full[sampling_rate*event_time:sampling_rate*(event_time+crop_duration)]

        # save
        op_file_name = op_dir + file_name[:-4] + '_' + str(jj) + '.wav'
        wavfile.write(op_file_name, sampling_rate, x_crop)

        # append file name with labels and crop time
        op_info.append(os.path.basename(op_file_name) + ', ' + str(event_time) + ', ' + event_label + ',')


# write cropped labels
with open(op_labels_file, mode='wt') as myfile:
    myfile.write('\n'.join(op_info))
