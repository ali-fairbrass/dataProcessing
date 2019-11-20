import datetime
import pandas as pd 


file_path = 'C:\\Users\\ucfaalf\\Dropbox\\EngD\\Funding\\EPSRC_Impact_Accelerator_Grant\\Data\\2017-07-18\\bat1.csv'
cur_data = pd.read_csv(file_path, sep=',', index_col=None, header=0)
cur_timestamp = cur_data.loc[:,'timestamp']
dates = [datetime.datetime.fromtimestamp(t // 1000) for t in cur_timestamp.values]
se = pd.Series(dates)
cur_data['new_col'] = se.values
# cur_data['date'], cur_data['time'] = zip(*cur_data['new_col'].map(lambda x: x.split(' ')))
print cur_data

