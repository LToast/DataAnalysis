install.packages("tidyverse")

library(factoextra)
library(FactoMineR)
library(tidyverse)
library(dplyr)

#data(dataframe)
#dataframe.active <- dataframe[, -c(3:4)]
#dataplot.PCA(res.pca, axes=c(1, 2), choix="ind")
frame.active <- dataframe.active[, -6]
#all
dataframe.active <- r
#top
dataframe.active <- r %>% top_n(8, Score)
#bot
dataframe.active <- r %>% top_n(-7, Score)
#moyenne
dataframe.active <- r %>% group_by(round(Score,0)) %>% 
                                     summarise_all("mean")

res.pca = PCA(dataframe.active, scale.unit=TRUE)
plot.PCA(res.pca, axes=c(1, 2), choix="ind")

fviz_eig(res.pca, addlabels = TRUE)

fviz_pca_var(res.pca,
             col.var = "contrib", 
             gradient.cols = c("#00AFBB", "#E7B800", "#FC4E07"),
             repel = TRUE     
)
