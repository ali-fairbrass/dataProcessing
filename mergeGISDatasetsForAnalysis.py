import pandas as pd

# OSM data
DIR = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\"

df = pd.read_csv(DIR + "Stage2 - dataProcessing\\amountLandGroupPerSite.csv")
df.rename(columns={'Site': 'SSS'}, inplace=True)

	# Amalgamate protected area values
PA_list = ['Protected Area', 'Forested Protected Area', 'Non-forested Protected Area']
df['Protected Area'] = df[PA_list].sum(axis=1)

col_list= list(df)
col_list.remove('SSS')

df['percentCover'] = (df.sum(axis=1) / 3140000) * 100
df.ix[df.percentCover > 100, 'percentCover'] = 100

df['Agricultural_Rounded'] = (df['Agricultural'] / (df[col_list].sum(axis=1) / 100)) * (3140000/100)
df['Blue Infrastructure_Rounded'] = (df['Blue Infrastructure'] / (df[col_list].sum(axis=1) / 100)) * (3140000/100)
df['Forested Green Infrastructure_Rounded'] = (df['Forested Green Infrastructure'] / (df[col_list].sum(axis=1) / 100)) * (3140000/100)
df['Impervious_Rounded'] = (df['Impervious'] / (df[col_list].sum(axis=1) / 100)) * (3140000/100)
df['Non-forested Green Infrastructure_Rounded'] = (df['Non-forested Green Infrastructure'] / (df[col_list].sum(axis=1) / 100)) * (3140000/100)
df['Protected Area_Rounded'] = (df['Protected Area'] / (df[col_list].sum(axis=1) / 100)) * (3140000/100)

# Nearest Non-impervious data

dfNearest = pd.read_csv(DIR + "TabelsfromGIS\\nearestNonImpervious.csv")
dfNearest = dfNearest[['SSS', 'Distance', 'type_group']]
dfNearest.rename(columns={'Distance': 'distanceNearest_nonImperv', 'type_group': 'nearest_nonImperv'}, inplace=True)

# Ecoregion data

dfEcoregion = pd.read_csv(DIR + "TabelsfromGIS\\sitesEcoregions.csv")
dfEcoregion = dfEcoregion[['SSS', 'WWF_REALM2', 'WWF_MHTNAM']]
dfEcoregion.rename(columns={'WWF_REALM2': 'ecoregionRealm', 'WWF_MHTNAM': 'ecoregionHabitat'}, inplace=True)

# Administrative data

dfAdminData = pd.read_csv(DIR + "TabelsfromGIS\\SitesCountryContinent.csv")
dfAdminData = dfAdminData[['SSS', 'admin', 'continent']]
dfAdminData.rename(columns={'admin': 'Country', 'continent': 'Continent'}, inplace=True)

# Study and phylum data

DIR1 = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\dataForAnalysis\\"
dfTaxon = pd.read_csv(DIR1 + "allKingdom.csv")
cols = list(dfTaxon.columns.values)[1:]
cols.insert(-3, 'Kingdom')
cols = cols[:-3]
dfTaxon = dfTaxon[cols]
dfTaxon.rename(columns={'Kingdom': 'TaxonKingdom'}, inplace=True)

# Merge dataframes and remove dulicate rows (duplicates caused by bug which dulpictes rows when dates are present in dataframe)

dfFinal = pd.merge(left=dfTaxon,right=dfAdminData, how='left', left_on='SSS', right_on='SSS')
dfFinal = pd.merge(left=dfFinal,right=dfEcoregion, how='left', left_on='SSS', right_on='SSS')
dfFinal = pd.merge(left=dfFinal,right=dfNearest, how='left', left_on='SSS', right_on='SSS')
dfFinal = pd.merge(left=dfFinal,right=df, how='left', left_on='SSS', right_on='SSS')
dfFinal = dfFinal.drop_duplicates()

# Replace NAs in OSM columns with zeros

col_list= list(df)
col_list.remove('SSS')
for column in col_list:
    dfFinal[column].fillna(0, inplace=True)

# Write to csv

dfFinal.to_csv(DIR + 'Stage2 - dataProcessing\\allKingdomData.csv', index = False, na_rep='NA')