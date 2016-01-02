# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 10:06:54 2015

@author: evgeniydonev
"""

import pandas as pd
import matplotlib.pyplot as plt
noef=pd.read_excel("Lux_assay.xlsx", 'noef')



means = noef.mean()
errors = noef.std()




fig, ax = plt.subplots()
#ax.get_xaxis().set_visible(False)   # Hide Ticks

means.plot(yerr=errors,table=False, ax=ax, kind='bar')
plt.title('NoEf')
#plt.xlabel('Cultures')
plt.ylabel('RLU/OD600')