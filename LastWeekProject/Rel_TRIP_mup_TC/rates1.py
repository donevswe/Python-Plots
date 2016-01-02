# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:20:22 2015

@author: ev
"""

import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def ploting(x,y):
    
    fig=plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y,color='r',label='$ %s$' % 'Find 0.5 conc')
    ax.legend(fontsize=16)
    ax.legend(fontsize=16)
    ax.set_xlim([-1,max(x)]) 
    ax.set_yscale('linear',fontsize=16)
    ax.set_xscale('log',fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    ax.set_xlim([0,100]) 
    ax.set_ylim([0.2,1.1])
    plt.ylabel('Kn/K1',fontsize=16)
    plt.xlabel('[Trim]',fontsize=16)
    ax.grid(True)   





conc=[64,32,16,8,4,2,1,0.5,0]

noef=pd.read_excel("rates1.xlsx", 'Sheet1')


#noef1=noef.groupby('strain')
noef1=np.array(noef)
noef1=noef1.T
noef=pd.DataFrame(noef1)


ywt=noef[0][1:10]
ywtNo=noef[0][9]
ywt=ywt/ywtNo
ywt=np.array(ywt)

yrel=noef[1][1:10]
yrelNo=noef[1][9]
yrel=yrel/yrelNo
yrel=np.array(yrel)


#ploting(conc,ywt)
ploting(conc,yrel)


