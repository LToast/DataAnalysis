install.packages("tidyverse")

library(factoextra)
library(FactoMineR)
library(tidyverse)
library(dplyr)

#data(dataframe)
dataframe.active <- dataframe[, -c(2:4)]
dataframe.active <- dataframe[, -c(3:4)]

#dataplot.PCA(res.pca, axes=c(1, 2), choix="ind")
frame.active <- dataframe.active[, -6]
r3<-r[, -c(2,15)]

#all
dataframe.active <- r3
#top
dataframe.active <- r %>% top_n(8, Score)
dataframe.active <-dataframe.active[, -c(2,15)]

#bot
dataframe.active <- r %>% top_n(-7, Score)
#moyenne
dataframe.active <- r %>% group_by(round(Score,0)) %>% 
                                     summarise_all("mean")

dataframe.active <-dataframe.active[, -c(1,3,16)]

res.pca = PCA(dataframe.active, scale.unit=TRUE)
plot.PCA(res.pca, axes=c(1, 2), choix="ind")
eig.val <- get_eigenvalue(res.pca)
eig.val
fviz_eig(res.pca, addlabels = TRUE)

fviz_pca_var(res.pca,
             col.var = "contrib", 
             gradient.cols = c("#00AFBB", "#E7B800", "#FC4E07"),
             repel = TRUE     
)
