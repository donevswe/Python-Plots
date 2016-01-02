# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:55:05 2015

@author: ev
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#root = Tk() ; root.withdraw()
#file = filedialog.askopenfilename(parent=root)
#noef=pd.read_excel(file, 'all')
noef=pd.read_excel("lux_assay.xlsx", 'allTranspose')


noef1=noef.groupby('CULTURES')
means = noef1.mean()
errors = noef1.std()




fig, ax = plt.subplots(1)
#ax.get_xaxis().set_visible(False)   # Hide Ticks

means.plot(yerr=errors,table=False, ax=ax, kind='bar',fontsize=16)
plt.title('Data from Lux Assay (Mean & SD)',fontsize=16)
#plt.xlabel('Cultures')
plt.ylabel('RLU/OD600',fontsize=16)
plt.xlabel('CULTURES',fontsize=16)
