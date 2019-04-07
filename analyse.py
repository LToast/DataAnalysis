# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:28:30 2019

@author: Theo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tracks = pd.read_csv('dataframe.csv',sep=',',encoding='latin1')
tracks_numerical=tracks.drop(['Artist','Track Name'],axis=1)
tracks_numerical.describe()
tracks_numerical.boxplot(column='duration_ms')
tracks_numerical.boxplot(column='tempo')
tracks_numerical.boxplot(column='Score')
