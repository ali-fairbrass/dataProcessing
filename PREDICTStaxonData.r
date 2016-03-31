# Taxon data from PREDICTS

x <- readRDS("SiteDataClass.rds")

allClass <- do.call(rbind, x) # This one line turns the large list into a dataframe.

# Do the same or phylum and kingdom, merging the dataframes and discarding the duplicate columns

DIR <- "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\PREDICTS\\TaxonomicData\\"

write.csv(allClass, paste(DIR, "allClass.csv"), row.names=TRUE)












#Everything underneath is unneccessary

classList <- c("Agaricomycetes", "Arachnida", "Arthoniomycetes", "Aves", "Bryopsida", "Chilopoda", "Clitellata", "Diplopoda",
               "Dothideomycetes", "Entognatha", "Equisetopsida", "Eurotiomycetes", "Gastropoda", "Gnetopsida", "Insecta", "Jungermanniopsida",
               "Lecanoromycetes", "Liliopsida", "Magnoliopsida", "Malacostraca", "Mammalia", "Pauropoda", "Pinopsida", "Polypodiopsida")

classVector <- names(x)

Agaricomycetes <- x$Agaricomycetes
Arachnida <- x$Arachnida
Arthoniomycetes <- x$Arthoniomycetes
Aves <- x$Aves
Bryopsida <- x$Bryopsida
Chilopoda <- x$Chilopoda
Clitellata <- x$Clitellata
Diplopoda <- x$Diplopoda
Dothideomycetes <- x$Dothideomycetes
Entognatha <- x$Entognatha
Equisetopsida <- x$Equisetopsida
Eurotiomycetes <- x$Eurotiomycetes
Gastropoda <- x$Gastropoda
Gnetopsida <- x$Gnetopsida
Insecta <- x$Insecta
Jungermanniopsida <- x$Jungermanniopsida
Lecanoromycetes <- x$Lecanoromycetes
Liliopsida <- x$Liliopsida
Magnoliopsida <- x$Magnoliopsida
Malacostraca <- x$Malacostraca
Mammalia <- x$Mammalia
Pauropoda <- x$Pauropoda
Pinopsida <- x$Pinopsida
Polypodiopsida <- x$Polypodiopsida

DIR = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\PREDICTS\\TaxonomicData\\"

write.csv(Agaricomycetes, paste(DIR, "Agaricomycetes", ".csv"), row.names=FALSE)

for (i in 1:length(classList))
{
  write.csv(x[[i]], paste(DIR, classList[i], ".csv"), row.names=FALSE)
}


for (i in 1:length(classList))
{
  write.csv(x[[classList[i]]], paste(DIR, classList[i], ".csv"), row.names=FALSE)
}


x[[i]]



for (i in 1:length(classList)){ 
  temp <- x$classList[i]
  write.csv(temp, paste(DIR, classList[i], ".csv"), row.names=FALSE)
}

temp <- x$Polypodiopsida

for (i in 1:length(classList))
{print(x$Polypodiopsida)}

for (taxon in classList)
{
  print(x$taxon)
}
  

# Created individual files per class by hand (no loop becuase I dhate R and I can't be bothered to find out how to do a for loop)

Chilopoda$taxon_Class <- "Chilopoda"
Bryopsida_subset <- Chilopoda[, c(15, 21)]
#write.csv(df_subset, "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\PREDICTS\\TaxonomicData\\Magnoliopsida.csv",
 #         row.names=FALSE)

allClasses <- rbind(Arachnida_subset, Aves_subset, Insecta_subset, Lecanoromycetes_subset, Liliopsida_subset, Magnoliopsida_subset)

# Merge with full data file

siteData <- read.csv("C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\TablesforGIS\\CombinedData_PREDICTS_SR_Tom.csv",
                     header = T)

library(plyr)

df <- merge(siteData, allClasses[ , ], by.x="SSS", by.y="SSS", all=T)

write.csv(df, file = "C:\\Users\\ucfaalf\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\PREDICTS\\dataWithTaxonClasses.csv",
          row.names=FALSE)

# Tables from GIS

