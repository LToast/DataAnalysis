# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:28:30 2019

@author: Theo
"""

import numpy as np
import pandas as pd

tracks = pd.read_csv('dataframe.csv',sep=',',encoding='latin1')
tracks_numerical=tracks.drop(['Artist','id','Track Name'],axis=1)
tracks_numerical.describe()
tracks_numerical.boxplot(column='acousticness',by='score')