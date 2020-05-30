import pandas as pd
import numpy as np
import matplotlib as mpl
# mpl.style.use('ggplot')
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("Graduate Admissions.csv")

df = df[['GRE Score','TOEFL Score', 'Chance of Admit ']]
# shape = 500, 3

# GRE Score -> (290, 340)
#TOEFL Score -> (92, 120)
#Chance of Admit -> (0.34, 0.97)
print(df['TOEFL Score'].describe())
'''
fig = plt.figure()
ax = fig.add_subplot(111)

fit1 = np.polyfit(x = df['GRE Score'], y = df['Chance of Admit '], deg = 1)
fit2 = np.polyfit(x = df['TOEFL Score'], y = df['Chance of Admit '], deg = 1)
# df.plot(kind = 'scatter', x = 'GRE Score', y = 'Chance of Admit ', label = 'GRE')
# df.plot(kind = 'scatter', x = 'TOEFL Score', y = 'Chance of Admit ', label = 'TOEFL Score')

ax.scatter(x = df['GRE Score'], y = df['Chance of Admit '], label = 'GRE Score', c = 'orange')
ax.scatter(x = df['TOEFL Score'], y = df['Chance of Admit '], label = 'TOEFL Score', c = 'red')
plt.legend(loc = 'upper left')
#
x = df['GRE Score']
plt.plot(x, fit1[0] * x + fit1[1], color = 'black')
#
x = df['TOEFL Score']
plt.plot(x, fit2[0] * x + fit2[1], color = 'black')
#
#fit1[0] = 0.01012587106076457
#fit2[0] = 0.0183850310073353
plt.text(125, 0.9, r'$slope = 0.018$')
plt.text(295, 0.9, r'$slope = 0.010$')

plt.xlabel('Scores')
plt.ylabel('Chance of Admit')
plt.title('Variation of Chance of Admit with GRE and TOEFL Score')

plt.show()
'''
