import pandas as pd
import numpy as np
import matplotlib as mpl
# mpl.style.use('ggplot')
import matplotlib.pyplot as plt
from pywaffle import Waffle
import csv

df = pd.read_csv("Graduate Admissions.csv")

df = df[['Research', 'CGPA', 'Chance of Admit ']]

#CGPA avg = 8.57

#CGPA >= 9.0 is a high and below is low


df11 = df.loc[(df['Research'] == 1) & (df['CGPA'] < 9.0) & (df['Chance of Admit '] >= 0.9)]
df10 = df.loc[(df['Research'] == 1) & (df['CGPA'] < 9.0) & (df['Chance of Admit '] < 0.9)]

df01 = df.loc[(df['Research'] == 0) & (df['CGPA'] >= 9.0) & (df['Chance of Admit '] >= 0.9)]
df00 = df.loc[(df['Research'] == 0) & (df['CGPA'] >= 9.0) & (df['Chance of Admit '] < 0.9)]

df101 = df.loc[(df['Research'] == 1) & (df['CGPA'] >= 9.0) & (df['Chance of Admit '] >= 0.9)]
df100 = df.loc[(df['Research'] == 1) & (df['CGPA'] >= 9.0) & (df['Chance of Admit '] < 0.9)]

# df1.shape = 151
# df0.shape = 15
# df10.shape = 129

# df11 = df1.loc[df['Chance of Admit '] >= 0.9]
# df10 = df1.loc[df['Chance of Admit '] < 0.9]
#
# df01 = df0.loc[df['Chance of Admit '] >= 0.9]
# df00 = df0.loc[df['Chance of Admit '] < 0.9]
#
# df101 = df10.loc[df['Chance of Admit '] >= 0.9]
# df100 = df10.loc[df['Chance of Admit '] < 0.9]

data = {'A' : [0], 'B' : [151],
        'C' : [0], 'D' : [15],
        'E': [70], 'F': [59]}

df = pd.DataFrame(data)
df = df.transpose()

df.rename(columns = { 0 : 'data'}, inplace = True)

fig = plt.figure( FigureClass = Waffle, rows = 5,
                    values = df.data, labels = list(df.index),
                    figsize = (10, 5), legend = {'loc': 'upper left', 'bbox_to_anchor' : (1.1, 1)})


plt.title('Effect of CGPA and Research on Chance of Admit')
plt.show()

# print(df.head())
