# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 11:52:30 2015

@author: evgeniydonev
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
noef=pd.read_excel("lux_assay.xlsx", '2mp')



means = noef.mean()
errors = noef.std()




#fig, ax = plt.subplots()
#ax.get_xaxis().set_visible(False)   # Hide Ticks

#means.plot(yerr=errors,table=False, ax=ax, kind='bar')
sns.barplot( data=noef)
plt.title('2MP')
#plt.xlabel('Cultures')
plt.ylabel('RLU/OD600')