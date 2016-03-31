import numpy as np
import random
import csv
import itertools
import matplotlib.pyplot as plt
import pylab

results = np.genfromtxt('C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 4\\sampleSizeTests\\speciesRichnessDataForPythonIteration90.csv', delimiter=",")

def countSpecies(results):
    results.sum(axis = 0)
    totalSpecies = np.count_nonzero(results.sum(axis = 0))
    return totalSpecies

def getRandomSubset(results, populationSize, sampleSize):
    random_subset = results[np.random.randint(populationSize,size=sampleSize),:]
    return random_subset

def getSiteResults(resultsFile, recordsPerSite, numberOfSites, sampleSize, numberOfIterations):
    amalgamatedResults = []
    for i in xrange(0,(recordsPerSite*numberOfSites),recordsPerSite):
        finalResults = []
        first_row = i
        final_row = i + recordsPerSite
        site_results = results[first_row:final_row]
        for i in range(0, numberOfIterations): # iterate 100 times
            random_subset = getRandomSubset(site_results, recordsPerSite, sampleSize)
            totalSpecies = countSpecies(random_subset)
            finalResults.append(totalSpecies)
        amalgamatedResults.append([sampleSize, sum(finalResults)/len(finalResults), np.std(finalResults)])
    return amalgamatedResults

### Generate results for 100 iterations of each sample size for each site ###

minSampleSize = 5
maxSampleSize = 95
steps = 5
numberOfSites = 6
samplesPerSite = 90
numberOfIterations = 100
resultsOfIterations = []

for j in xrange(minSampleSize, maxSampleSize, steps):
    resultsOfIterations.append(getSiteResults(results, samplesPerSite, numberOfSites, j, numberOfIterations))


### Generate summary statistics for each sample size for each site ###

numberOfSampleSizes = 18
countDataIndex = 1
SDCountDataIndex = 2
numberOfSites = 6

summaryStats = []

for site in xrange(0, numberOfSites, 1):
    siteCounts = []
    siteSDs = []
    for i in xrange(0, numberOfSampleSizes, 1):
        siteCounts.append(resultsOfIterations[i][site][countDataIndex])
        siteSDs.append(resultsOfIterations[i][site][SDCountDataIndex])
    summaryStats.append(siteCounts + siteSDs)

### Generate sample sizes for plot axes

sampleTimes = []
for i in xrange(5, 95, 5):
    sampleTimes.append(i)

# Create list of site names for plot titles

siteNames = ["CR8", "E105JP", "HA86RB", "RM143YB", "SW112PN", "W84LA"]

### Generate plots ###

fig, axarr = plt.subplots(nrows=3, ncols=2, sharex=True, figsize=(15,15))

for index, ax in enumerate(axarr.ravel()):
    ax.errorbar(sampleTimes, summaryStats[index][:18], yerr=summaryStats[index][18:])
    countPlusSD = max(summaryStats[index][18:])+max(summaryStats[index][:18])
    print countPlusSD
    pylab.ylim([0, countPlusSD])
    pylab.xlim([0,95])
    ax.set_title(siteNames[index])
fig.text(0.5, 0.04, 'Sample size (minutes)', ha='center')
fig.text(0.04, 0.5, '           Average species richness\nError bars indicate standard deviation', va='center', rotation='vertical')

### Save plots as png file ###

fig.savefig('C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 4\\sampleSizeTests\\speciesRichnessAveragesWithReplacement90.png')