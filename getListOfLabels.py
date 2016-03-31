import os
import csv
from collections import Counter

CSV_DIR = 'C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 3\\goldenTestSet\\'

Ali19 = os.listdir(CSV_DIR + "19VerityLabels\\Ali")
Verity19 = os.listdir(CSV_DIR + "19VerityLabels\\Verity")
Jiemin19 = os.listdir(CSV_DIR + "19VerityLabels\\Jiemin")
Verity21 = os.listdir(CSV_DIR + "21VerityLabels\Verity")

Ali19List = []
for csvFile in Ali19:
    filePath = CSV_DIR + '19VerityLabels\\Ali\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            Ali19List.append(row[1])

Verity19List = []
for csvFile in Verity19:
    filePath = CSV_DIR + '19VerityLabels\\Verity\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            Verity19List.append(row[1])

Jiemin19List = []
for csvFile in Jiemin19:
    filePath = CSV_DIR + '19VerityLabels\\Jiemin\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            Jiemin19List.append(row[1])

Verity21List = []
for csvFile in Verity21:
    filePath = CSV_DIR + '21VerityLabels\\Verity\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            Verity21List.append(row[1])

CSV_DIR1 = "C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Data\\"

allLabels2013 = os.listdir(CSV_DIR1 + "2013Random\\allLabelFiles")

allLabels2014 = os.listdir(CSV_DIR1 + "2014Random\\allLabelFiles")

allLabels2015 = os.listdir(CSV_DIR1 + "2015Random\\allLabelFiles")

all2013List = []
for csvFile in allLabels2013:
    filePath = CSV_DIR1 + '2013Random\\allLabelFiles\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            all2013List.append(row[1])

all2014List = []
for csvFile in allLabels2014:
    filePath = CSV_DIR1 + '2014Random\\allLabelFiles\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            all2014List.append(row[1])

all2015List = []
for csvFile in allLabels2015:
    filePath = CSV_DIR1 + '2015Random\\allLabelFiles\\' + csvFile
    with open(filePath, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            all2015List.append(row[1])


mergedList = Ali19List + Verity19List + Jiemin19List + Verity21List + all2013List + all2014List + all2015List
print Counter(mergedList)
# print sorted(list(set(mergedList)))
# print len(list(set(mergedList)))

#with open(CSV_DIR + "listOfLabels.csv", 'wb') as myfile:
 #   wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  #  wr.writerow(sorted(list(set(mergedList))))

