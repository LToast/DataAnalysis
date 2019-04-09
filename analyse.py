# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:28:30 2019

@author: Theo
"""
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

tracks = pd.read_csv('dataframe.csv',sep=',',encoding='latin1')
tracks_numerical=tracks.drop(['Artist','Track Name','Unnamed: 0'],axis=1)
tracks_numerical['Score'].describe()
sns.distplot(tracks_numerical['Score'])
score=np.log(tracks_numerical['Score'])
score.describe()
sns.distplot(score)
score=(score - np.mean(score)) / np.std(score)
score.describe()
sns.distplot(score)
df = tracks_numerical



n_components = 18
 
# Do the PCA.
pca = PCA(n_components=n_components)
reduced = pca.fit_transform(df)
 
# Append the principle components for each entry to the dataframe
for i in range(0, n_components):
    df['PC' + str(i + 1)] = reduced[:, i]
 
display(df.head())

g = sns.lmplot(
    'PC1',
    'PC2',
       data=df,
       hue='Score',
    fit_reg=False,
    scatter=True,
    size=7,
    )
 
plt.show()
 
# Plot a variable factor map for the first two dimensions.
(fig, ax) = plt.subplots(figsize=(12, 12))
for i in range(0, len(pca.components_)):
    ax.arrow(0, 0,  # Start the arrow at the origin
             pca.components_[0, i], pca.components_[1, i],  # 0 and 1 correspond to dimension 1 and 2
             head_width=0.1,head_length=0.1)
    plt.text(pca.components_[0, i] + 0.05, pca.components_[1, i] + 0.05, df.columns.values[i])
 
an = np.linspace(0, 2 * np.pi, 100)  # Add a unit circle for scale
plt.plot(np.cos(an), np.sin(an))
plt.axis('equal')
ax.set_title('Variable factor map')
plt.show()

