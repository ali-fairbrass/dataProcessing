import os
import csv
from collections import Counter

# CSV_DIR = 'C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 3\\goldenTestSet\\'

# Ali19 = os.listdir(CSV_DIR + "19VerityLabels\\Ali")
# Verity19 = os.listdir(CSV_DIR + "19VerityLabels\\Verity")
# Jiemin19 = os.listdir(CSV_DIR + "19VerityLabels\\Jiemin")
# Verity21 = os.listdir(CSV_DIR + "21VerityLabels\Verity")

# Ali19List = []
# for csvFile in Ali19:
#     filePath = CSV_DIR + '19VerityLabels\\Ali\\' + csvFile
#     with open(filePath, 'rb') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             Ali19List.append(row[1])

# Verity19List = []
# for csvFile in Verity19:
#     filePath = CSV_DIR + '19VerityLabels\\Verity\\' + csvFile
#     with open(filePath, 'rb') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             Verity19List.append(row[1])

# Jiemin19List = []
# for csvFile in Jiemin19:
#     filePath = CSV_DIR + '19VerityLabels\\Jiemin\\' + csvFile
#     with open(filePath, 'rb') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             Jiemin19List.append(row[1])

# Verity21List = []
# for csvFile in Verity21:
#     filePath = CSV_DIR + '21VerityLabels\\Verity\\' + csvFile
#     with open(filePath, 'rb') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             Verity21List.append(row[1])

CSV_DIR1 = "Y:\\Fieldwork_Data\\"

allLabels2013 = os.listdir(CSV_DIR1 + "2013\\Random_Files_Process\\SM2BAT+_Labels")

allLabels2014Church = os.listdir(CSV_DIR1 + "2014\\Random_25\\Churchyard\\SM2BAT+_Labels")

allLabels2014GreenRoof = os.listdir(CSV_DIR1 + "2014\\Random_25\\GreenRoof\\SM2BAT+_Labels")

allLabels2015 = os.listdir(CSV_DIR1 + "2015\\Random_25\\SM2BAT+lables")

all2013List = []
for csvFile in allLabels2013:
    filePath = CSV_DIR1 + '2013\\Random_Files_Process\\SM2BAT+_Labels\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            all2013List.append(row[1])

all2014ChurchList = []
for csvFile in allLabels2014Church:
    filePath = CSV_DIR1 + '2014\\Random_25\\Churchyard\\SM2BAT+_Labels\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            all2014ChurchList.append(row[1])

all2014GreenRoofList = []
for csvFile in allLabels2014GreenRoof:
    filePath = CSV_DIR1 + '2014\\Random_25\\GreenRoof\\SM2BAT+_Labels\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            all2014GreenRoofList.append(row[1])

all2015List = []
for csvFile in allLabels2015:
    filePath = CSV_DIR1 + '2015\\Random_25\\SM2BAT+lables\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            all2015List.append(row[1])


#mergedList = Ali19List + Verity19List + Jiemin19List + Verity21List + all2013List + all2014List + all2015List

mergedList = all2013List + all2014ChurchList + all2014GreenRoofList + all2015List

# print Counter(mergedList)
labelFrequency = list(Counter((mergedList)).items())
print labelFrequency
# print sorted(list(set(mergedList)))
# print len(list(set(mergedList)))

CSV_DIR = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter4\\Data\\ultrasonic\\"

with open(CSV_DIR + "listOfLabels.csv", 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(['Label', 'Frequency'])
    for row in labelFrequency:
        wr.writerow(row)
