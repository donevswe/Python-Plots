# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:44:08 2015

@author: ev
"""

import numpy as np
from pandas import ExcelWriter
#import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from polyTRim1 import polyfit

time=np.array([0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660])
#Create the first item froeach key
dbase={} 
data=pd.read_excel('output'+str(0)+'.xlsx', 'Sheet1') 
data=np.array(data)
for i in range(len(data)):
    for ii in range(len(data[i])):
        x=str(i)+str(ii)
        dat=[]
        dat.append(data[i][ii])
        dbase[x]=dat
        

for i in range(1,len(time)):
    data=pd.read_excel('output'+str(i)+'.xlsx', 'Sheet1') 
    data=np.array(data)
    for i in range(len(data)):
        for ii in range(len(data[i])):
            x=str(i)+str(ii)

            temp=dbase[x]
            temp.append(data[i][ii])      # mutates the copy
            dbase[x] = temp


def strainKeys(col):
    wt=[]
    relA=[]
    
    for key in sorted(dbase.keys()):
        if key[1]==str(col) and int(key[0]) in [0,1,2]:
            wt.append(key)
        elif key[1]==str(col) and int(key[0]) in [3,4,5]:
            relA.append(key)
    return wt, relA       
            

def KeysDat(keys):
    strainDatCol=[]  
    for key in keys:
        strainDatCol.append(np.array(dbase[key]))
        
    return strainDatCol


        

def ploting(dat,strain,farg, col):
    dat=pd.DataFrame(dat)
    men=dat.mean()
    
    #print(str(col))
    #print(men)
    sd=dat.std()
    fig=plt.figure()
    ax = fig.add_subplot(111)
    ax.errorbar(time, men,yerr=sd,color=farg,label='$'+str(strain)+'- %s$' % str(col))
    ax.legend(fontsize=16)
    ax.set_xlim([-1,max(time)+100]) 
    ax.set_ylim([0.04,0.8])
    
    ax.set_yscale('log',fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    plt.ylabel('OD600_',fontsize=16)
    plt.xlabel('Time(min)',fontsize=16)
    ax.grid(True)    

def polynome(x,y,n, name):
    y=pd.DataFrame(y)
    y=y.mean()
    
    #print(y)
    polyfit(x[2:6], y[2:6], n, name, c=False) 




TrashKeysWT, TrashKeysREL =strainKeys(9)
TrashWT=KeysDat(np.array(TrashKeysWT))
TrashREL=KeysDat(np.array(TrashKeysREL))

colors=['b', 'g', 'r', 'c','m','y', 'k', 'w', 'b','g']
for color, i in zip(colors, range(10)): # 10= the number of columns
    wt0key, rel0key=  strainKeys(i)
    wt0=KeysDat(wt0key)
    #wt0=np.array(wt0)-np.array(TrashWT)
    
    rel0 =KeysDat(rel0key)
    #rel0=np.array(rel0)-np.array(TrashREL)
    
    ploting(wt0,'wt',color, i)   
    ploting(rel0,'rel',color, i)
    
    #polynome(time,np.log(wt0),len(time) , 'wt'+str(i) )
    #polynome(time,np.log(rel0),len(time) , 'rel0'+str(i) )
   