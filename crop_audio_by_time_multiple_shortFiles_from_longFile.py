import pandas as pd
import numpy as np
from scipy.io import wavfile
import os
import glob
from datetime import datetime

data_dir = "Z:\\KateJonesgroup\\Ali\\Fieldwork_Data\\2015\\"
op_dir = 'X:\\Fieldwork_Data\\2015\\'

# folders = os.listdir(data_dir)
# folders.remove('BR20EG')
# folders.remove('BR28LB')
# folders.remove('BR67US')
folders = ['SM2+']

startTime = datetime.now()

crop_duration = 60.0  # seconds

for folder in folders:
    data_folder = data_dir + folder #+ "\\SM2+\\"
    op_folder = op_dir + folder + "\\SM2+_Sliced\\"

    if not os.path.exists(op_folder):
        os.makedirs(op_folder)

    audio_files = glob.glob(data_folder + '*.wav')

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
            op_file_name = op_folder + file_name[:-4] + str(i) + '.wav'
            wavfile.write(op_file_name, sampling_rate, x_crop)
            
print 'Time taken:' + str(datetime.now() - startTime)