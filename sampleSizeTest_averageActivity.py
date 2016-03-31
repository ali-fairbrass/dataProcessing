import numpy as np
import random
import csv
import itertools
import matplotlib.pyplot as plt
import pylab

minSampleSize = 5
maxSampleSize = 30
steps = 5
numberOfSites = 15
recordsPerSite = 25
numberOfIterations = 100
resultsOfIterations = []

# Results file must be single column of avtivity values without column header
results = np.genfromtxt('C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 4\\sampleSizeTests\\activityBiophonySingleColumn.csv',  delimiter=",")

def getRandomSubset(results, sampleSize):
    random_subset = np.random.choice(results, sampleSize, replace=True)
    return random_subset

def getSiteResults(resultsFile, recordsPerSite, numberOfSites, sampleSize, numberOfIterations):
    amalgamatedResults = []
    for i in xrange(0, (recordsPerSite*numberOfSites), recordsPerSite):
        finalResults = []
        first_row = i
        final_row = i + recordsPerSite
        site_results = results[first_row:final_row]
        for i in xrange(0, numberOfIterations): # iterate 100 times
            random_subset = getRandomSubset(site_results, sampleSize)
            averageActivity = sum(random_subset)/len(random_subset)
            finalResults.append(averageActivity)
        amalgamatedResults.append([sampleSize, sum(finalResults)/len(finalResults), np.std(finalResults)])
    return amalgamatedResults

for j in xrange(minSampleSize, maxSampleSize, steps):
    resultsOfIterations.append(getSiteResults(results, recordsPerSite, numberOfSites, j, numberOfIterations))

######################################### Generate Plots ####################################################

numberOfSampleSizes = 5
averageActivityDataIndex = 1
SDActivityDataIndex = 2
numberOfSites = 15

summaryStats = []

for site in xrange(0, numberOfSites, 1):
    siteAverages = []
    siteSDs = []
    for i in xrange(0, numberOfSampleSizes, 1):
        siteAverages.append(resultsOfIterations[i][site][averageActivityDataIndex])
        siteSDs.append(resultsOfIterations[i][site][SDActivityDataIndex])
    summaryStats.append(siteAverages + siteSDs)

sampleTimes = []
for i in xrange(5, 30, 5):
    sampleTimes.append(i)
print sampleTimes

siteNames = ["CR05EF", "CR8", "E105JP", "E47EN", "HA53AA", "HA86RB", "NW1", "RM143YB", "SE23", "SE3", "SW112PN", "SW154LA", "W112NN", "W84LA", "WC2H8LG"]

fig, axarr = plt.subplots(nrows=5, ncols=3, sharex=True, figsize=(15,15))

for index, ax in enumerate(axarr.ravel()):
    ax.errorbar(sampleTimes, summaryStats[index][:5], yerr=summaryStats[index][5:])
    pylab.ylim([0,(max(summaryStats[index][5:])+(max(summaryStats[index][:5])))])
    pylab.xlim([0,30])
    ax.set_title(siteNames[index])
fig.text(0.5, 0.04, 'Sample size (minutes)', ha='center')
fig.text(0.04, 0.5, 'Average anthropogenic sound activity (occupied spectrogram pixels)\n                  Error bars indicate standard deviation', va='center', rotation='vertical')

# Save fig, enter file path

fig.savefig('.png')