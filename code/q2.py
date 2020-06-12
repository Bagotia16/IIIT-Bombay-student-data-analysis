import numpy as np
import pandas as pd
import matplotlib as mpl
# mpl.use('agg')
from matplotlib import pyplot
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("Graduate Admissions.csv")

df = df[['GRE Score','TOEFL Score', 'Research']]
#shape = (500, 3)

df1 = df.loc[df['Research'] > 0]
df0 = df.loc[df['Research'] == 0]

#histogram comparing GRE1 and GRE0
# pyplot.hist(x = df1['GRE Score'], bins = 30, alpha = 0.5, label = 'With Research Experience', color = 'green')
# pyplot.hist(x = df0['GRE Score'], bins = 30, alpha = 0.5, label = 'No Research Experience', color = 'gray')
# pyplot.legend(loc = 'upper left')
#
# pyplot.show()

#histogram comparing TOEFL1 and TOEFL0
# pyplot.hist(x = df1['TOEFL Score'], bins = 30, alpha = 0.5, label = 'With Research Experience', color = 'green')
pyplot.hist(x = df0['TOEFL Score'], bins = 30, alpha = 0.5, label = 'No Research Experience', color = 'gray')
pyplot.legend(loc = 'upper left')

# print(df0.describe())
# print(df1.describe())

plt.xlabel('TOEFL Score')
plt.ylabel('Frequency of Occurence')
plt.title('Score dependency on Research')

pyplot.show()
