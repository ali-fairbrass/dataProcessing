import pandas as pd
import csv

#Combine label amounts csv with indices file

indicesFile = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 2 Acoustic analysis\\Results\\25_Files\\AcousticIndices\\acousticDiversity_RM143YB_SM2.csv"

labelAmountFile = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 2 Acoustic analysis\\Results\\25_Files\\LabelAmounts\\RM143YB_LabelAmounts_All.csv"

labelAmountFileTransport = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 2 Acoustic analysis\\Results\\25_Files\\LabelAmounts\\441kHz_LabelAmounts_Transport.csv"

combinedFile = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 2 Acoustic analysis\\Results\\25_Files\\CombinedFiles\\RM143YB_acousticDiversity_LabelAmounts.csv"

combinedFileAllLabels = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 2 Acoustic analysis\\Results\\25_Files\\CombinedFiles\\441kHz_acousticDiversity_LabelAmounts_All.csv"

#Indices with non-transport
df1 = pd.read_csv(indicesFile)
df2 = pd.read_csv(labelAmountFile)
merged = df1.merge(df2, on="FILENAME", how="outer").fillna("")
merged.to_csv(combinedFile, index=False)

#And adding transport labels
df1 = pd.read_csv(combinedFile)
df2 = pd.read_csv(labelAmountFileTransport)
merged = df1.merge(df2, on="FILENAME", how="outer").fillna("")
merged.to_csv(combinedFileAllLabels, index=False)

#Combine csv files based on a common header

combined441kHz = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 2 Acoustic analysis\\Results\\25_Files\\CombinedFiles\\441kHz_acousticDiversity_LabelAmounts_All.csv"
combined24kHz = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 2 Acoustic analysis\\Results\\25_Files\\CombinedFiles\\24kHz_acousticDiversity_LabelAmounts_All.csv"

one = DataFile(combined24kHz)
two = DataFile(combined441kHz)
one.get_header()

comb = set(one.get_header() + two.get_header())
final = list(one.with_header(comb)) + list(two.with_header(comb))
final

# f = open(combined24kHz, 'r')
# reader = csv.reader(f)
# # set first line as header
# header24kHz = [x.strip() for x in reader.next()]

# comb = set(header24kHz + header441kHz)
# final = list(header24kHz.with_header(comb)) + list(header441kHz.with_header(comb))

# # def get_header(header):
# #         return header

# def with_header(headers):
#     """ Returns a generator for specified headers"""
#     header_dict = dict([(a, i,) for i, a in enumerate(header)])

#     for line in reader:
#         li = []
#         for h in headers:
#             if h in header_dict:
#                 li.append(line[header_dict[h]])
#             else:
#                 li.append(empty)
#         yield li

#DataFile class from http://stackoverflow.com/questions/25224790/merge-multiple-csv-file-based-on-a-template-header-in-python
import csv
class DataFile(object):
    empty = ''  # use this if col does not have value

    def __init__(self, filename):
        f = open(filename, 'r')
        self.reader = csv.reader(f)
        # set first line as header
        self.header = [x.strip() for x in self.reader.next()]

    def get_header(self):
        return self.header

    def with_header(self, headers):
        """ Returns a generator for specified headers"""
        header_dict = dict([(a, i,) for i, a in enumerate(self.header)])

        for line in self.reader:
            li = []
            for h in headers:
                if h in header_dict:
                    li.append(line[header_dict[h]])
                else:
                    li.append(self.empty)
            yield li