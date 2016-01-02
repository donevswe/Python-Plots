# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 11:56:44 2015

@author: evgeniydonev
"""

import pandas as pd
import matplotlib.pyplot as plt
noef=pd.read_excel("lux_assay.xlsx", '4ep')



means = noef.mean()
errors = noef.std()




fig, ax = plt.subplots()
#ax.get_xaxis().set_visible(False)   # Hide Ticks

means.plot(yerr=errors,table=False, ax=ax, kind='bar')
plt.title('4EP')
#plt.xlabel('Cultures')
plt.ylabel('RLU/OD600')