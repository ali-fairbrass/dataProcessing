# Merge 2013 csv label files

import os
import pandas as pd
import csv

ROOT_DIR = "C:\\Users\\ucfaalf\\Documents\\Projects\\AcousticAnalysis\\2013Random\\"

aliLabels2013 = os.listdir(ROOT_DIR + "LabelsCSV")

jieminLabels2013 = os.listdir(ROOT_DIR + "LabelsCSVTransport")

wavFiles2013 = os.listdir(ROOT_DIR + "Amalgamated_Files")

filesInBothLabelLists = set(aliLabels2013).intersection(jieminLabels2013)

for wavFile in wavFiles2013:

	if wavFile[:-4] + '-sceneRect.csv' in filesInBothLabelLists:
		print wavFile
		df_jiemin = pd.read_csv(ROOT_DIR + "LabelsCSVTransport\\" + wavFile[:-4] + '-sceneRect.csv')
		df_ali = pd.read_csv(ROOT_DIR + "LabelsCSV\\" + wavFile[:-4] + '-sceneRect.csv')

		bothDataframes = [df_jiemin, df_ali]

		result = pd.concat(bothDataframes)

		OUT_FILE = ROOT_DIR + "Labels_AliAndJiemin\\" + wavFile[:-4] + '-sceneRect.csv'

		result.to_csv(OUT_FILE, sep=',', index=False)

	else:
		pass