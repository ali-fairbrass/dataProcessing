import numpy as np
import random
import csv
import itertools
import matplotlib.pyplot as plt
import pylab

minSampleSize = 5
maxSampleSize = 65
steps = 5
numberOfSites = 6
samplesPerSite = 60
numberOfIterations = 100
resultsOfIterations = []

# Results file must be binary matrix without column header or row names
results = np.genfromtxt('C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 4\\sampleSizeTests\\speciesRichnessDataForPythonIteration.csv', delimiter=",")

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

# Get results of iterations
for j in xrange(minSampleSize, maxSampleSize, steps):
    print j
    resultsOfIterations.append(getSiteResults(results, samplesPerSite, numberOfSites, j, numberOfIterations))

######################################### Generate Plots ####################################################

numberOfSampleSizes = 12
countDataIndex = 1
SDCountDataIndex = 2
numberOfSites = 6

summaryStats = []

for site in xrange(0, numberOfSites, 1):
    print "site: " + str(site)
    siteCounts = []
    siteSDs = []
    for i in xrange(0, numberOfSampleSizes, 1):
        print "Iteration: " + str(i)
        siteCounts.append(resultsOfIterations[i][site][countDataIndex])
        print "Site average: " + str(siteCounts)
        siteSDs.append(resultsOfIterations[i][site][SDCountDataIndex])
        print "Site SD: " + str(siteSDs)
    summaryStats.append(siteCounts + siteSDs)

sampleTimes = []
for i in xrange(5, 65, 5):
    sampleTimes.append(i)

siteNames = ["CR8", "E105JP", "HA86RB", "RM143YB", "SW112PN", "W84LA"]	

fig, axarr = plt.subplots(nrows=3, ncols=2, sharex=True, figsize=(15,15))

for index, ax in enumerate(axarr.ravel()):
    ax.errorbar(sampleTimes, summaryStats[index][:12], yerr=summaryStats[index][12:])
    countPlusSD = max(summaryStats[index][12:])+max(summaryStats[index][:12])
    print countPlusSD
    pylab.ylim([0, countPlusSD])
    pylab.xlim([0,65])
    ax.set_title(siteNames[index])
fig.text(0.5, 0.04, 'Sample size (minutes)', ha='center')
fig.text(0.04, 0.5, '           Average species richness\nError bars indicate standard deviation', va='center', rotation='vertical')

# Save fig, enter file path

fig.savefig('.png')