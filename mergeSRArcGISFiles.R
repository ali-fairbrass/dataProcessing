df1 <- read.csv("C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\TabelsfromGIS\\AllSitesGI.csv", header=T)
df2 <- read.csv("C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\TabelsfromGIS\\ModelOutput_BI.csv", header=T)
df3 <- read.csv("C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Data\\TabelsfromGIS\\OSM_CountryData_Nearest_GI.csv", header=T)

mergedf <- merge(df1, df2[ , c("SSS", "AREA_GEO")], by.x = "Site", by.y = "SSS", all.x =T)

mergedf <- merge(mergedf, df3[ , c("SSS", "GI_type", "Distance")], by.x = "Site", by.y = "SSS", all.x =T)

merge(x = DF1, y = DF2[ , c("Client", "LO")], by = "Client", all.x=TRUE)

mergedf[is.na(mergedf)] <- 0

colnames(mergedf)[125] <- "blueInfrastructure"
colnames(mergedf)[126] <- "nearest_GI_type"
colnames(mergedf)[127] <- "nearest_GI_distance"

write.csv(mergedf, file = "C:\\Users\\ucfaalf\\Documents\\Dropbox\\EngD\\Projects\\Chapter 1 Systematic Review\\Author Contact\\Information obtained from authors\\Herrmann_2012\\rerequestforinformationherrmannetal_2012paper\\city_gall_merged.csv",
          row.names=FALSE)