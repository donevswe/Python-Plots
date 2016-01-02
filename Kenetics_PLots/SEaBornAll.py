# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:38:23 2015

@author: ev
"""

import os 
import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#root = Tk() ; root.withdraw()
#file = filedialog.askopenfilename(parent=root)
#noef=pd.read_excel(file, 'all')
noef=pd.read_excel("lux_assay.xlsx", 'all')


li=('WT','A','B','C')

for it in li:
    plt.figure()
    
    sns.barplot(x='CULTURES', y= it,data=noef)
    plt.legend(it, loc = "upper left", title = "cat")