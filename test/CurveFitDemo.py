# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:22:08 2019

@author: Trevor Sleight
"""

#Clear the memory to eliminate any old variables. 
get_ipython().magic('reset -sf')

import os
import pandas as pd
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

##****************************************
df = pd.read_excel(r"C:\ResearchWorkingDirectory\WhiteNoise.xlsx", sheet_name = 'SinWave')

dataX = df['X']
dataY = df['Y2']

optimize_func = lambda x: x[0]*np.sin(x[1]*dataX+x[2]) + x[3] - dataY

#Basic Guesses to Get the optomization Stared
guess_mean = np.mean(dataY)
guess_std = 3*np.std(dataY)/(2**0.5)/(2**0.5)
guess_phase = 0
guess_freq = 1
guess_amp = 1

#first guess 
data_first_guess = guess_std*np.sin(dataX+guess_phase) + guess_mean

est_amp, est_freq, est_phase, est_mean = leastsq(optimize_func, [guess_amp, guess_freq, guess_phase, guess_mean])[0]

#plot the raw data
plt.scatter(dataX, dataY)

data_fit = est_amp*np.sin(est_freq*dataX+est_phase) + est_mean

#plotting commands
plt.plot(dataX, data_first_guess, label='first guess', color = 'orange')
plt.plot(dataX, data_fit, label='after fitting', color = 'red')
plt.show()

