import pandas as pd
import numpy as np
import matplotlib as mpl
# mpl.style.use('ggplot')
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("Graduate Admissions.csv")

df = df[['University Rating', 'LOR ', 'CGPA', 'Research']]

df = df.loc[(df['CGPA'] <9.0) & (df['Research'] == 0)]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter(x = df['LOR '], y = df['University Rating'])

plt.xlabel('LOR Score')
plt.ylabel('University Rating')
plt.title('Effect of LOR on University Rating')

plt.show()
