import pandas as pd
import numpy as np
from scipy.io import wavfile
import os
import glob

def cropSM2Files(inputdirectory, outputdirectory):

    crop_duration = 60.0  # seconds

    if not os.path.exists(outputdirectory):
        os.makedirs(outputdirectory)

    audio_files = glob.glob(inputdirectory + "\\" + '*.wav')

    for ii, file_name_full in enumerate(audio_files):
        
        for i in xrange(30):
            
            start_time = str(i*6) + str(.0) # seconds    

            file_name = os.path.basename(file_name_full)
            sampling_rate, x_full = wavfile.read(file_name_full)
            file_duration = x_full.shape[0] / float(sampling_rate)

            print '\n', os.path.basename(file_name), start_time

    #         crop
            x_crop = x_full[sampling_rate*float(start_time):sampling_rate*(float(start_time)+crop_duration)]

            # save
            op_file_name = outputdirectory + "\\" + file_name[:-4] + str(i) + '.wav'
            wavfile.write(op_file_name, sampling_rate, x_crop)


# SM2Folders = ['BR4', 'N17', 'DA5', 'RM41PL']
# for folder in SM2Folders:
#     cropSM2Files("F:\\Fieldwork_Data\\2015\\" + folder + "\\SM2+", "X:\\Fieldwork_Data\\2015\\" + folder + "\\SM2+_Sliced")
                
cropSM2Files("Z:\\KateJonesgroup\\Ali\\Fieldwork_Data\\2015\\TN147QB\\SM2+", "Y:\\Fieldwork_Data\\2015\\TN147QB\\SM2+_Sliced")
                