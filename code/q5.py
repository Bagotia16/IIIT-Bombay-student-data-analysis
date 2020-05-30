import pandas as pd
import numpy as np
import matplotlib as mpl
# mpl.style.use('ggplot')
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("Graduate Admissions.csv")

#Chance of Admit -> (0.34, 0.97)
# University Rating out of 5 -> (1, 5)
df = df[['University Rating', 'Chance of Admit ']]

#shape = (500, 2)

df1 = df.loc[df['University Rating'] == 1]
#df1.shape = (34, 2)
df2 = df.loc[df['University Rating'] == 2]
#df2.shape = (126, 2)
df3 = df.loc[df['University Rating'] == 3]
#df3.shape = (162, 2)
df4 = df.loc[df['University Rating'] == 4]
#df4.shape = (105, 2)
df5 = df.loc[df['University Rating'] == 5]
#df5.shape = (73, 2)


fig = plt.figure()
ax = fig.add_subplot(111)
#
# ax.scatter(x = df1['University Rating'], y = df1['Chance of Admit '], label = '1')
# ax.scatter(x = df2['University Rating'], y = df2['Chance of Admit '], label = '2')
# ax.scatter(x = df3['University Rating'], y = df3['Chance of Admit '], label = '3')
# ax.scatter(x = df4['University Rating'], y = df4['Chance of Admit '], label = '4')
# ax.scatter(x = df5['University Rating'], y = df5['Chance of Admit '], label = '5')
#
# plt.legend(loc = 'upper left')

data_to_plot = [df1['Chance of Admit '], df2['Chance of Admit '], df3['Chance of Admit '], df4['Chance of Admit '], df5['Chance of Admit ']]


# df1['Chance of Admit '].plot(kind = 'box')
# df2['Chance of Admit '].plot(kind = 'box')
bp = ax.boxplot(data_to_plot, patch_artist = True)

ax.set_xticklabels(['University rating=1', 'University rating=2', 'University rating=3', 'University rating=4', 'University rating=5'])
plt.ylabel('Chance of Admit')
plt.title('Effect of University Rating on Chance of Admission')



ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

for box in bp['boxes']:
    box.set(color = 'blue', linewidth = 2)
    box.set(facecolor = 'grey')

for whisker in bp['whiskers']:
    whisker.set(color = 'black', linewidth = 2)

for cap in bp['caps']:
    cap.set(color = 'black', linewidth = 2)

for median in bp['medians']:
    median.set(color = 'red', linewidth = 2)

for flier in bp['fliers']:
    flier.set(marker = 'o', color = 'orange', alpha = 0.5)

plt.show()
