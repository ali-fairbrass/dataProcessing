import pandas as pd

DIR = "C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\TabelsfromGIS\\Continents\\"
df = pd.read_csv(DIR + "resultsContinents.csv")

DIR1 = "C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\"
conversionTable = pd.read_csv(DIR1 + "Stage2 - dataProcessing\\OSMtypesToGroupsForAnalysis.csv")
conversionTable.drop('Method Code', axis=1, inplace=True)
conversionTable.drop('Methods', axis=1, inplace=True)

groupsToConvertTo = ['Agricultural', 'Blue Infrastructure', 'Forested Green Infrastructure', 'Forested Protected Area', 
                     'Impervious', 'Non-forested Green Infrastructure', 'Non-forested Protected Area', 'Protected Area']

landTypes = list(df.columns.values)[1:]

conversionList = conversionTable.values.tolist()

def assignCalculationsPerType(listOfCalculationPerType):
    
    convertToSingleGroup = []
    splitBetweenTwoGroups = []
    splitBetweenThreeGroups = []
    splitBetweenFourGroups = []
    
    for i in xrange(0, len(listOfCalculationPerType), 1):
        if listOfCalculationPerType[i][1] <= 2:
            convertToSingleGroup.append(listOfCalculationPerType[i][0])
        elif listOfCalculationPerType[i][1] == 3:
            splitBetweenTwoGroups.append(listOfCalculationPerType[i][0])
        elif listOfCalculationPerType[i][1] == 4:
            splitBetweenThreeGroups.append(listOfCalculationPerType[i][0])
        else:
            splitBetweenFourGroups.append(listOfCalculationPerType[i][0])
        
    return convertToSingleGroup, splitBetweenTwoGroups, splitBetweenThreeGroups, splitBetweenFourGroups

def getGITypesPerGroup(listOfTypes, GIgroup, listOfCalculationPerType):
    typesForCalculation = []
    for i in xrange(0, len(listOfTypes), 1):
        if GIgroup in listOfCalculationPerType[i][2:]:
            typesForCalculation.append(listOfCalculationPerType[i][0])
        else:
            pass
    return list(set(typesForCalculation))

def getCalculationGroupsPerGIGroup(listOfTypesForGIGroup, calcType1, calcType2, calcType3, calcType4):
    calcType1GIGroup = []
    calcType2GIGroup = []
    calcType3GIGroup = []
    calcType4GIGroup = []
    for GItype in listOfTypesForGIGroup:
        if GItype in calcType1:
            calcType1GIGroup.append(GItype)
        elif GItype in calcType2:
            calcType2GIGroup.append(GItype)
        elif GItype in calcType3:
            calcType3GIGroup.append(GItype)
        elif GItype in calcType4:
            calcType4GIGroup.append(GItype)
        else:
            pass
    return calcType1GIGroup, calcType2GIGroup, calcType3GIGroup, calcType4GIGroup


for GIgroup in groupsToConvertTo:
    
    typesForGIGroup = getGITypesPerGroup(landTypes, GIgroup, conversionList)
    
    calcType1, calcType2, calcType3, calcType4 = assignCalculationsPerType(conversionList)
    
    group1, group2, group3, group4 = getCalculationGroupsPerGIGroup(typesForGIGroup, calcType1, calcType2, calcType3, calcType4)
    
    df[GIgroup] = df[group1].sum(axis=1) + df[group2].sum(axis=1)/2 + df[group3].sum(axis=1)/3 + df[group4].sum(axis=1)/4


groupsToConvertTo.insert(0,'Site')
df = df[groupsToConvertTo]
df.to_csv(DIR1 + "Stage2 - dataProcessing\\amountLandGroupPerSite.csv", index=False)