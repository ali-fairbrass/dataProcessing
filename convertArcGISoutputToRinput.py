# Create site by GI area table from ArcGIS output table

import csv
import pandas as pd
import numpy as np
import itertools

def loadCSVFile(filepath):
	loadedFile = []

	with open(filepath, 'rb') as csvfile:
	    csvfile.next() # skip the header
	    reader = csv.reader(csvfile, delimiter=',')
	    for row in reader:
	        loadedFile.append(row)

	return loadedFile


def getGIType(csvfile):
    
    GItype =[]

    for row in csvfile:
        GItype.append([row[2]])
    
    GItype_set = set(map(tuple,GItype))  #need to convert the inner lists to tuples so they are hashable
    GIlist = map(list,GItype_set) #Now convert tuples back into lists (maybe unnecessary?)
    
    return GIlist

# Get list of all sites, site with and without GI

def siteWandWoGI(studiesFile, resultFile):
    
    allSites = []
    for row in studiesFile:
        allSites.append(row[14])
        
    sitesWGI_duplicates = []
    for row in resultFile:
        sitesWGI_duplicates.append(row[1])
        
    sitesWGI = list(set(sitesWGI_duplicates))

    sitesWOGI = []
    for site in allSites:
        if site not in sitesWGI:
            sitesWOGI.append(site)
                   
    return allSites, sitesWGI, sitesWOGI


def createResultsForSitesWGI(listOfSitesWGI, results, GIlist):
	siteWGIresults = []
	    
	for site in listOfSitesWGI:
	    siteResults = []
	    # print "site: " + str(site)

	    for result in results:
	        if result[1] == site:
	            siteResults.append(result)
	        else:
	            pass   
	        
	    for result in siteResults:
	        row = []
	        row.append(result[1])
	        for GItype in GIlist:
	            if [result[2]] == GItype:
	            	row.append(result[-1])
	              
	                print "Site: " + str(site) + "with GI type " + str(GItype) + " of area " + str(result[-1])
	            else:
	            	# print "GI area: " + str("0")
	                row.append('0')
	        print "Row of results: " + str(row)
	        siteWGIresults.append(row)

	return siteWGIresults

def createResultsForSitesWOGI(listofSitesWOGI, GIlist):
	siteWOGIresults = []
	for site in listofSitesWOGI:
		row = []
		row.append(site)
		for GItype in GIlist:
			row.append('0')
		siteWOGIresults.append(row)

	return siteWOGIresults	

def mergeResultsToDataframe(siteWGIresults, siteWOGIresults, GIlist):
	mergedGIlist = list(itertools.chain(*GIlist))
	mergedGIlist.insert(0, "Site")
	columnHeader = mergedGIlist

	n = np.array(siteWGIresults)
	df = pd.DataFrame(n, columns = columnHeader)
	df_withGI = df.groupby("Site").sum()

	n = np.array(siteWOGIresults)
	df_withoutGI = pd.DataFrame(n, columns = columnHeader)

	df_AllSites = pd.concat([df_withGI, df_withoutGI])

	return df_AllSites

def writeResultsToCSV(resultsDataframe, outputFileDir, outputFileName):
	
	resultsDataframe.to_csv(outputFileDir + "/" + outputFileName + ".csv", sep=',')

def GItableFromArcGISOutput(ArcGISfilepath, studiesfilepath, resultsFileDirectory, resultsFileName):
	results = loadCSVFile(ArcGISfilepath)
	studies = loadCSVFile(studiesfilepath)
	GIlist = getGIType(results)
	allSites, sitesWGI, sitesWOGI = siteWandWoGI(studies, results)
	listOfSitesWithGIAreasAndZeros = createResultsForSitesWGI(sitesWGI, results, GIlist)
	listOfSitesWithoutGIAreasAndZeros = createResultsForSitesWOGI(sitesWOGI, GIlist)
	results_DF = mergeResultsToDataframe(listOfSitesWithGIAreasAndZeros, listOfSitesWithoutGIAreasAndZeros, GIlist)
	writeResultsToCSV(results_DF, resultsFileDirectory, resultsFileName)

GItableFromArcGISOutput("C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\TabelsfromGIS\\ModelOutput_GI_Behrmann.csv",
	"C:\\Users\\ucfaalf\\Dropbox\\EngD\Projects\\Chapter 1 Systematic Review\\Data\TablesforGIS\\CombinedData_PREDICTS_SR_Tom.csv",
	"C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\TabelsfromGIS", "AllSitesGI_Behrmann")

