import pandas as pd

filePath = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\TabelsfromGIS\\ModelOutput_nonGeofabrik_GIandBI.csv"

df = pd.read_csv(filePath)

sites = sorted(set(df["SSS"].tolist()))
GI_types = sorted(set(df["type_overlap_GI_BI"].tolist()))

results = []

for site_index, site in enumerate(sites):
    print "Site: number " + str(site_index) + " of " + str(len(sites)) + " sites"
    row = []
    row.append(site)
    site_df= df[df['SSS'] == site]
    for GI in GI_types:

		GI_subset = site_df[site_df['type_overlap_GI_BI'] == GI]
		if GI_subset.empty:
			row.append('0')
		else:

			row.append(str(GI_subset.iloc[0]['Area_Calc']))

    results.append(row)


GI_types_list = list(GI_types)
GI_types_list.insert(0, "Site")
df_results = pd.DataFrame(results, columns=GI_types_list)

DIR = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\TabelsfromGIS\\"

df_results.to_csv(DIR + "results_nonGeofabrik_GIandBI.csv")