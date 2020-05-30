import pandas as pd
import numpy as np
import matplotlib as mpl
# mpl.style.use('ggplot')
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("Graduate Admissions.csv")

#Chance of Admit -> (0.34, 0.97)
# SOP -> (1, 5)
# LOR -> (1, 5)
df = df[['SOP', 'LOR ', 'Chance of Admit ']]
# shape = (500, 3)

# we are putting a threshold here to define who is 'admitted' and who is not
df = df.loc[df['Chance of Admit '] >= 0.6]

#shape = (405, 3)

print(df.describe())

#               SOP        LOR   Chance of Admit
# count  405.000000  405.000000        405.000000
# mean     3.601235    3.679012          0.771630
# std      0.867952    0.846179          0.102253
# min      1.500000    1.500000          0.600000
# 25%      3.000000    3.000000          0.690000
# 50%      3.500000    3.500000          0.760000
# 75%      4.500000    4.500000          0.860000
# max      5.000000    5.000000          0.970000
