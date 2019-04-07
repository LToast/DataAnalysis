# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 12:00:10 2019

@author: Theo
"""
from sklearn.decomposition import pca
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#récupération de toutes les données
scrap = pd.read_csv("scrap.csv")
tracks_spotify =  pd.read_csv('track_details_spot.csv')
dataset = pd.read_csv('dataLight.csv')
#selection de la region
dfr = dataset[dataset.Region=="fr"]
dfr=dfr.drop(["Region"],axis=1)
#échantillon des données pour 2017 (365 jours)
dfr=dfr [(dataset.Date < '2018-01-01')]
#on a pour chaque chanson une ligne par jour dans le classement top200
#pour chaque chanson, on récupère la somme des stream, la position médiane et le nombre de jour
#où cette chanson était dans le classement
aggregation = dfr.groupby(['URL']).agg({'Streams' : np.sum,'Position' : np.mean,'Date':np.size})
dfr_unique=dfr.get(['Artist','Track Name','URL']).drop_duplicates(subset=['URL'])
agg_title=aggregation.merge(dfr_unique,on="URL")
#on extrait le track id de l'url pour la jointure
agg_title["id"]=agg_title["URL"].str.split("/").str[4]

full = agg_title.merge(scrap, on="id")
full["Score"] = full.Date / full.Position
#transformation de duration_ms en duration
full['duration']=round(full['duration_ms']/1000,0)

full = full.drop(["Unnamed: 0", "Position", "Date","duration_ms","URL","id","analysis_url","track_href","type","uri"], axis=1)
full.to_csv("dataframe.csv",sep=",", encoding='utf-8')
