# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 17:50:32 2015

@author: evgeniydonev
"""

from tkinter import *
from tkinter import filedialog
import os 
import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#root = Tk() ; root.withdraw()
#file = filedialog.askopenfilename(parent=root)
#noef=pd.read_excel(file, 'all')
noef=pd.read_excel("lux_assay.xlsx", 'all')


noef1=noef.groupby('CULTURES')
means = noef1.mean()
errors = noef1.std()




fig, ax = plt.subplots(1)
#ax.get_xaxis().set_visible(False)   # Hide Ticks

means.plot(yerr=errors,table=False, ax=ax, kind='bar',fontsize=16)
plt.title('Data from Lux Assay (Mean & SD)',fontsize=16)
#plt.xlabel('Cultures')
plt.ylabel('RLU/OD600',fontsize=16)
plt.xlabel('MEDIA',fontsize=16)



#means.to_excel('means.xlsx','Sheet1')
#errors.to_excel('errors.xlsx','Sheet1')

#Slicing Cool
men=means[1:3]
a=np.array(means)
df = pd.DataFrame(data=a[1:,2:],columns=['B','C','D'],index=['MP', 'NoeEf'])
fig.savefig('scipy_331_ex1.pdf', bbox_inches='tight')

##---------------------------------------------------------------------------------


