# import os
# import glob
# import shutil
# import csv

# # wavFileList = []
# # labelFileList = []

# # DIR = "C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Data\\2013Random\\"
# # wavFiles = os.listdir(DIR + "extra30From6_24kHz")
# # labelFiles = os.listdir(DIR + "extra30From6_labels")

# # for wavFile in wavFiles:
# # 	wavFileList.append(wavFile[:-4])
# # print wavFileList

# # for label in labelFiles:
# # 	labelFileList.append(label[:-14])
# # print labelFileList

# # birdWav = [x for x in wavFileList if x in labelFileList]
# # print birdWav

# # for i in birdWav:
# # 	print "Copying " + str(i)
# # 	shutil.copy(DIR + "extra30From6_24kHz\\" + str(i) + ".wav", DIR + "extra30from6_birdFiles")

# # #Write filenames to csv file
# # with open(DIR + '\\birdFiles.csv', 'wb') as f:
# #     writer = csv.writer(f)
# #     writer.writerows([sorted(birdWav)])
