import os
import glob
import shutil
import random

first25FileSelection = os.listdir("C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\Amalgamated_Files")

sixSites = ['W8_4LA', 'CR8', 'E10_5JP', 'HA8_6RB', 'RM14 3YB', 'SW11_2PN']

for site in sixSites:
    dirExtention = "Y:\\Fieldwork_Data\\2013\\" + site + "\\SM2+_Sliced"
    fileList = os.listdir(dirExtention)
    fileListMinusFirst25 = [x for x in fileList if x not in first25FileSelection]

    randomNumbers = random.sample(xrange(len(fileListMinusFirst25)), 35)
    fileSelection = [fileList[i] for i in randomNumbers]

    for i in fileSelection:
        shutil.copy(i, "C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\35From6Sites")

