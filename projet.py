# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 12:00:10 2019

@author: Theo
"""
import numpy as np
import pandas as pd


#récupération de toutes les données
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
aggregation = dfr.groupby(['Track Name']).agg({'Streams' : np.sum,'Position' : np.mean,'Date':np.size})
dfr_unique=dfr.get(['Artist','Track Name','URL']).drop_duplicates(subset=['Track Name'])
agg_title=aggregation.join(dfr_unique.reset_index().set_index("Track Name"))
#on extrait le track id de l'url pour la jointure
agg_title["id"]=agg_title["URL"].str.split("/").str[4]
#jointure ave le fichier d'analyse des chansons
join = agg_title.reset_index().set_index("id").join(tracks_spotify.set_index("id")).dropna()
df=join.drop(["URL","Unnamed: 0","analysis_url","deezer_id","track_href","type","uri"],axis=1)