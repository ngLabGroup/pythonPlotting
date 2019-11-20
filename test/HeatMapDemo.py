# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:22:08 2019

@author: Trevor
"""
get_ipython().magic('reset -sf')


import os

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
#from matplotlib.cm import cm

df = pd.read_excel(r"C:\ResearchWorkingDirectory\WhiteNoise.xlsx", sheet_name = 'Sheet1')
#great a left to right heatmap

x = df['X']
y = df['Y']
z = x+y

plt.scatter(x, y, c=z, cmap='jet')

plt.show()






