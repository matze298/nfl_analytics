# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 15:08:35 2018

@author: matze
"""

#%% Import libraries
import pandas as pd
import numpy as np
import tensorflow as tf

#%% Settings
season = 2017
team = 'GB'
#%% Read-in csv
df = pd.read_csv('data/nfl.csv')
# Print colum names
columns = list(df)
print(columns)
#%% 
data = df[df['Season'] == season]
data = data[data['posteam']==team]