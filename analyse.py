# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:28:30 2019

@author: Theo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  
import math as math

tracks = pd.read_csv('dataframe.csv',sep=',',encoding='latin1')
tracks_numerical=tracks.drop(['Artist','Track Name'],axis=1)
tracks_numerical['Score'].describe()
tracks_numerical['score_log']=math.log(tracks_numerical['Score'].astype(float))
plt.boxplot(tracks_numerical['Score'])
tracks_numerical.boxplot(column='tempo')
tracks_numerical.boxplot(column=['Score'],by='tempo')
bplot = sns.boxplot(y='Score', x='key', 
                 data=tracks_numerical, 
                 width=0.5,
                 palette="colorblind")
bplot = sns.boxplot(y='Score', x='mode', 
                 data=tracks_numerical, 
                 width=0.5,
                 palette="colorblind")