import pandas as pd

# OSM data

DIR = "C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\"
df = pd.read_csv(DIR + "Stage2 - dataProcessing\\amountLandGroupPerSite.csv")
df.rename(columns={'Site': 'SSS'}, inplace=True)

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

# Study and class data

DIR1 = "C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\dataForAnalysis\\"
dfTaxon = pd.read_csv(DIR1 + "allClass.csv")
cols = list(dfTaxon.columns.values)[1:]
cols.insert(-3, 'Class')
cols = cols[:-3]
dfTaxon = dfTaxon[cols]
dfTaxon.rename(columns={'Class': 'TaxonClass'}, inplace=True)

# Merge dataframes

dfFinal = pd.merge(left=dfTaxon,right=dfAdminData, how='left', left_on='SSS', right_on='SSS')
dfFinal = pd.merge(left=dfFinal,right=dfEcoregion, how='left', left_on='SSS', right_on='SSS')
dfFinal = pd.merge(left=dfFinal,right=dfNearest, how='left', left_on='SSS', right_on='SSS')
dfFinal = pd.merge(left=dfFinal,right=df, how='left', left_on='SSS', right_on='SSS')

# Write to csv

dfFinal.to_csv(DIR + 'Stage2 - dataProcessing\\allClassData.csv', index = False, na_rep='NA')