# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 00:15:39 2015

@author: ev
"""


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns


noef=pd.read_excel("lux_assay.xlsx", 'AL')


fig1=plt.figure(1)

sns.barplot(x="MEDIA", y="ABS", hue="CULTURES", data=noef);

plt.ylabel('RLU/OD600',fontsize=16)
plt.xlabel('MEDIA',fontsize=16)
fig1.savefig('BraPlotAllSeaborn.pdf', bbox_inches='tight')

fig2=plt.figure(2)
sns.factorplot(x="MEDIA", y="ABS", hue="CULTURES", data=noef);
fig2.savefig('Bra2.pdf')
