library(ggplot2)
library(vegan)
library(RVAideMemoire)
library(plyr)
library(tidyr)
library(data.table)
library(zoo)
library(RColorBrewer)
library(viridis)

setwd("/Volumes/EXPANSION/30-736680336/bin_summaries")

# read in the taxonomy csv 
table <- read.csv(file = "bin_counts_phylum_pooled.csv", row.names = 1, header = TRUE)
table <- decostand(table, method = "total")
table <- as.matrix(table)

rownames <- rownames(table)
colnames <- colnames(table)

write.csv(colnames, file = "Phylum_names.csv")

table <- melt(table)
names(table)[names(table)=="Var1"] <- "Species"
names(table)[names(table)=="Var2"] <- "Phylum"
names(table)[names(table)=="value"] <- "Relative_Abundance"

p <- ggplot(table) + geom_bar(aes(x = Species, y = Relative_Abundance, fill = Phylum), stat = "identity")
p + scale_fill_viridis_d(option="B") + 
  theme(plot.background = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank()) + ggtitle("Taxonomic Abudances from MAG's")

