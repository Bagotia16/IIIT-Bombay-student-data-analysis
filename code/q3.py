import pandas as pd
import numpy as np
import matplotlib as mpl
# mpl.style.use('ggplot')
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("Graduate Admissions.csv")

df = df[['University Rating', 'SOP', 'LOR ']]
# SOP -> (1, 5)
# LOR -> (1, 5)
# University Rating out of 5 -> (1, 5)

df1 = df.loc[df['University Rating'] == 1]
df2 = df.loc[df['University Rating'] == 2]
df3 = df.loc[df['University Rating'] == 3]
df4 = df.loc[df['University Rating'] == 4]
df5 = df.loc[df['University Rating'] == 5]

plt.bar([0.83, 1.83, 2.83, 3.83, 4.83], [df1['SOP'].mean(), df2['SOP'].mean(), df3['SOP'].mean(), df4['SOP'].mean(), df5['SOP'].mean()], label = "SOP Score", color = 'b', width = 0.3)
plt.bar([1.13, 2.13, 3.13, 4.13, 5.13], [df1['LOR '].mean(), df2['LOR '].mean(), df3['LOR '].mean(), df4['LOR '].mean(), df5['LOR '].mean()], label = "LOR Score", color = 'g', width = 0.3)
plt.legend()
plt.xlabel('University Ratings')
plt.ylabel('Average SOP and LOR Score')
plt.title('Variation of SOR and LOR Score with University Rating')

plt.show()
