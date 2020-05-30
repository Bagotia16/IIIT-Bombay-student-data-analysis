import pandas as pd
import numpy as np
import matplotlib as mpl
# mpl.style.use('ggplot')
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("Graduate Admissions.csv")

df = df[['Research', 'Chance of Admit ']]

df1 = df.loc[df['Research'] == 1]
df0 = df.loc[df['Research'] == 0]

df91 = df1.loc[df['Chance of Admit '] >= 0.9]
df81 = df1.loc[(df['Chance of Admit '] >= 0.8) & (df['Chance of Admit '] < 0.9)]
df71 = df1.loc[(df['Chance of Admit '] >= 0.7) & (df['Chance of Admit '] < 0.8)]
df61 = df1.loc[(df['Chance of Admit '] >= 0.6) & (df['Chance of Admit '] < 0.7)]
df51 = df1.loc[(df['Chance of Admit '] >= 0.5) & (df['Chance of Admit '] < 0.6)]
df41 = df1.loc[(df['Chance of Admit '] >= 0.4) & (df['Chance of Admit '] < 0.5)]
df31 = df1.loc[(df['Chance of Admit '] >= 0.3) & (df['Chance of Admit '] < 0.4)]

df90 = df0.loc[df['Chance of Admit '] >= 0.9]
df80 = df0.loc[(df['Chance of Admit '] >= 0.8) & (df['Chance of Admit '] < 0.9)]
df70 = df0.loc[(df['Chance of Admit '] >= 0.7) & (df['Chance of Admit '] < 0.8)]
df60 = df0.loc[(df['Chance of Admit '] >= 0.6) & (df['Chance of Admit '] < 0.7)]
df50 = df0.loc[(df['Chance of Admit '] >= 0.5) & (df['Chance of Admit '] < 0.6)]
df40 = df0.loc[(df['Chance of Admit '] >= 0.4) & (df['Chance of Admit '] < 0.5)]
df30 = df0.loc[(df['Chance of Admit '] >= 0.3) & (df['Chance of Admit '] < 0.4)]

data1 = { 'Chance of Admit' : [df91.shape[0], df81.shape[0], df71.shape[0], df61.shape[0], df51.shape[0], df41.shape[0], df31.shape[0]],
            "index" : ['>=0.9', '0.9>()>=0.8', '0.8>()>=0.7', '0.7>()>=0.6', '0.6>()>=0.5', '0.5>()>=0.4', '0.4>()>=0.3']}

data0 = { 'Chance of Admit' : [df90.shape[0], df80.shape[0], df70.shape[0], df60.shape[0], df50.shape[0], df40.shape[0], df30.shape[0]],
            "index" : ['>=0.9', '0.9>()>=0.8', '0.8>()>=0.7', '0.7>()>=0.6', '0.6>()>=0.5', '0.5>()>=0.4', '0.4>()>=0.3']}

# df1 = pd.DataFrame(data1)
# df1 = df1[['Chance of Admit', 'index']]

df0 = pd.DataFrame(data0)
df0 = df0[['Chance of Admit', 'index']]

# df1.set_index("index", inplace = True)
df0.set_index("index", inplace = True)

color_list = ['blue', 'orange', 'lightgreen', 'lightcoral', 'yellow', 'black', 'red']
# explode_list = [0 , 0, 0, 0, 0.1, 0.1, 0.1]
# df1['Chance of Admit'].plot( kind = 'pie', autopct = '%1.1f%%', figsize = (15, 6),
#                             startangle = 130, shadow = False, labels = None,
#                             pctdistance = 1.12, explode = explode_list, colors = color_list)

# plt.title('Variation of Chance of Admit in Research group')
# plt.axis('equal')
# plt.legend(labels = df1.index, loc = 'upper left')

explode_list = [0.1 , 0.1, 0, 0, 0, 0.1, 0.1]
df0['Chance of Admit'].plot( kind = 'pie', autopct = '%1.1f%%', figsize = (15, 6),
                            startangle = 150, shadow = False, labels = None,
                            pctdistance = 1.12, explode = explode_list)

plt.title('Variation of Chance of Admit in Non-Research group')
plt.axis('equal')
plt.legend(labels = df0.index, loc = 'upper left')

plt.show()
