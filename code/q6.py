import pandas as pd
import numpy as np
import matplotlib as mpl
# mpl.style.use('ggplot')
from matplotlib import pyplot
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("Graduate Admissions.csv")

df = df[['GRE Score', 'TOEFL Score', 'SOP', 'LOR ', 'CGPA', 'Chance of Admit ']]

df = df.loc[df['Chance of Admit '] >= 0.9]

pyplot.hist(x = df['TOEFL Score'], bins = 12, alpha = 0.7, label = 'TOEFL Score', color = 'blue')

pyplot.legend(loc = 'upper left')

plt.xlabel('TOEFL Score')
plt.ylabel('Frequency above 0.9% chance')
plt.title('TOEFL Score distribution above 0.9% Chance of Admit')

plt.show()
