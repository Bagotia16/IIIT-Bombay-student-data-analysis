import pandas as pd
import numpy as np
import matplotlib as mpl
# mpl.use('agg')
import matplotlib.pyplot as plt
from pywaffle import Waffle
import csv

df = pd.read_csv("Graduate Admissions.csv")

df = df[['GRE Score', 'LOR ']]

df1 = df.loc[(df['GRE Score'] >=290) & (df['GRE Score'] < 295)]
df2 = df.loc[(df['GRE Score'] >=295) & (df['GRE Score'] < 300)]
df3 = df.loc[(df['GRE Score'] >=300) & (df['GRE Score'] < 305)]
df4 = df.loc[(df['GRE Score'] >=305) & (df['GRE Score'] < 310)]
df5 = df.loc[(df['GRE Score'] >=310) & (df['GRE Score'] < 315)]
df6 = df.loc[(df['GRE Score'] >=315) & (df['GRE Score'] < 320)]
df7 = df.loc[(df['GRE Score'] >=320) & (df['GRE Score'] < 325)]
df8 = df.loc[(df['GRE Score'] >=325) & (df['GRE Score'] < 330)]
df9 = df.loc[(df['GRE Score'] >=330) & (df['GRE Score'] < 335)]
df10 = df.loc[(df['GRE Score'] >=335) & (df['GRE Score'] <= 340)]

x = [290, 295, 300, 305, 310, 315, 320, 325, 330, 335]
y = [2.40, 2.67, 2.86, 3.22, 3.35, 3.22, 3.82, 3.86, 4.23, 4.46]

plt.plot(x, y, color = 'green', linewidth = 3,
        marker = 'o', markerfacecolor = 'blue', markersize = 12)
plt.xlabel('GRE Score')
plt.ylabel('LOR Score')
plt.title('Variation of LOR with GRE Score')

plt.show()
