# Acau1 heatmap viz
library(ggplot2)
library(viridis)
library(viridisLite)
library(RColorBrewer)
library(reshape2)
setwd("/Volumes/EXPANSION/R_viz")

###############################################################################
# importing denitrification data
denitrification_table <- read.csv(file = "denitrification_KO_counts_pooled.csv", row.names = 1)
denitrification_table <- as.matrix(denitrification_table)

d_denitrification <- melt(denitrification_table)
ggp <- ggplot(d_denitrification,aes(Var1,Var2)) + geom_tile(aes(fill = value)) + scale_fill_viridis(option="D")
ggp + ggtitle(label = "Denitrification KO Counts") + labs(x = "Species", y = "Genes")


################################################################################
# nitrification data
nitrification_table <- read.csv(file = "nitrification_KO_counts_pooled.csv", row.names = 1)
nitrification_table <- as.matrix(nitrification_table)

nitrification_d <- melt(nitrification_table)

ggp_nirification <- ggplot(nitrification_d,aes(Var1,Var2)) + geom_tile(aes(fill = value)) + scale_fill_viridis(option="D")
ggp_nirification + ggtitle("Nitrification KO Counts") + labs(x = "Species", y = "Genes")

################################################################################
# nitrogen fixation data

Nfix_table <- read.csv(file = "N_fixation_counts.csv", row.names = 1)
Nfix_table <- as.matrix(Nfix_table)

Nfix_d <- melt(Nfix_table)

ggp_Nfix <- ggplot(Nfix_d,aes(Var1,Var2)) + geom_tile(aes(fill = value)) + scale_fill_viridis(option="viridis")
ggp_Nfix + ggtitle("N Fixation KO Counts") + labs(x = "Species", y = "KO Orthologs")

################################################################################
# assimilatory n reeduction data

ass_N_red_table <- read.csv(file = "ANR_KO_counts_pooled.csv", row.names = 1)
ass_N_red_table <- as.matrix(ass_N_red_table)

ass_N_red_d <- melt(ass_N_red_table)

ggp_ass_N_red <- ggplot(ass_N_red_d,aes(Var1,Var2)) + geom_tile(aes(fill = value)) + scale_fill_viridis(option="viridis")
ggp_ass_N_red + ggtitle("Assimilatory Nitrate Reduction KO Counts") + labs(x = "Species", y = "Genes")

################################################################################
# dissimilatory n reeduction data

dis_N_red_table <- read.csv(file = "DNR_KO_counts_pooled.csv", row.names = 1)
dis_N_red_table <- as.matrix(dis_N_red_table)

dis_N_red_d <- melt(dis_N_red_table)

ggp_dis_N_red <- ggplot(dis_N_red_d,aes(Var1,Var2)) + geom_tile(aes(fill = value)) + scale_fill_viridis(option="viridis")
ggp_dis_N_red + ggtitle("Dissimilatory Nitrate Reduction KO Counts") + labs(x = "Species", y = "Genes")

################################################################################
# annamox data

annamox_table <- read.csv(file = "annamox_counts.csv", row.names = 1)
annamox_table <- as.matrix(annamox_table)

annamox_d <- melt(annamox_table)

ggp_annamox <- ggplot(annamox_d,aes(Var1,Var2)) + geom_tile(aes(fill = value)) + scale_fill_viridis(option="viridis")
ggp_annamox + ggtitle("Annamox KO Counts") + labs(x = "Species", y = "KO Orthologs")




############## PIES ###############################################


denitrification_df <- data.frame(value = c(1,1,1,1,1,1),
                 group = c("Acau","Acon","Aful","Vrig","Xmut","Wfilter"))
denitrification_pie <- ggplot(denitrification_df, aes(x="",y=value, fill=group)) + geom_col(color="black") + coord_polar(theta="y")
denitrification_pie 


###################################################################
# 
nitrification_df <- data.frame(value = c(1,1,1,1,1,1),
                                 group = c("Acau","Acon","Aful","Vrig","Xmut","Wfilter"))
nitrification_pie <- ggplot(nitrification_df, aes(x="",y=value, fill=group)) + geom_col(color="black") + coord_polar(theta="y")
nitrification_pie 

###################################################################
# nobody
Nfix_df <- data.frame(value = c(1,1,1,1,1,1),
                               group = c("Acau","Acon","Aful","Vrig","Xmut","Wfilter"))
Nfix_pie <- ggplot(Nfix_df, aes(x="",y=value, fill=group)) + geom_col(color="black") + coord_polar(theta="y")
Nfix_pie 

################################################################################
# assimilatory n reeduction
# nobody
ass_N_red_df <- data.frame(value = c(1,1,1,1,1,1),
                      group = c("Acau","Acon","Aful","Vrig","Xmut","Wfilter"))
ass_N_red_pie <- ggplot(ass_N_red_df, aes(x="",y=value, fill=group)) + geom_col(color="black") + coord_polar(theta="y")
ass_N_red_pie 

################################################################################
# dissimilatory n reeduction

dis_N_red_df <- data.frame(value = c(1,1,1),
                           group = c("Acau","Xmut","Wfilter"))
dis_N_red_pie <- ggplot(dis_N_red_df, aes(x="",y=value, fill=group)) + geom_col(color="black") + coord_polar(theta="y")
dis_N_red_pie 
