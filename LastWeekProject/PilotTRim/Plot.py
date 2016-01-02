# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 21:58:09 2015

@author: ev
"""
import numpy as np
from pandas import ExcelWriter
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


import shelve
dbase = shelve.open("mydbase")


b=[]
for i in range(10):
    b.append([])


time=[0,60,120,120,180,240,300,360,420]
#Here the data is soted by column
for culture in sorted(dbase):
    
    if int(culture[4:])==0:
        b[0].append(dbase[culture])
    elif int(culture[4:])==1:
        b[1].append(dbase[culture])
    elif int(culture[4:])==2:
        b[2].append(dbase[culture])
    elif int(culture[4:])==3:
        b[3].append(dbase[culture])
    elif int(culture[4:])==4:
        b[4].append(dbase[culture])
    elif int(culture[4:])==5:
        b[5].append(dbase[culture])
    elif int(culture[4:])==6:
        b[6].append(dbase[culture])
    elif int(culture[4:])==7:
        b[7].append(dbase[culture])
    elif int(culture[4:])==8:
        b[8].append(dbase[culture])
    elif int(culture[4:])==9:
        b[9].append(dbase[culture])
        
b=np.array(b)

#Here the data is soted by cells
myda={}
for i in range(len(b)):
    for ii in range(len(b[-1])):
        c=str(i)
        v=str(ii)
        myda[v+c]=b[i][ii]

#Extracting keys wt or rel from a column        
def strainKeys(col):
    wt=[]
    relA=[]
    
    for key in sorted(myda.keys()):
        if key[1]==str(col) and int(key[0]) in [0,1,2]:
            wt.append(key)
        elif key[1]==str(col) and int(key[0]) in [3,4,5]:
            relA.append(key)
    return wt, relA       
            

def KeysDat(keys):
    strainDatCol=[]     
    for key in keys:
        strainDatCol.append(myda[key])
    return strainDatCol

def ploting(dat,strain,col):
    dat=pd.DataFrame(dat)
    men=dat.mean()
    sd=dat.std()
    fig=plt.figure()
    ax = fig.add_subplot(111)
    ax.errorbar(time, men,yerr=sd,color='r',label='$'+str(strain)+'- %s$' % str(col))
    ax.legend(fontsize=16)
    ax.set_xlim([-1,max(time)+100]) 
    ax.set_ylim([-5,4])
    
    ax.set_yscale('linear',fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    plt.ylabel('OD600_',fontsize=16)
    plt.xlabel('Time(min)',fontsize=16)
    ax.grid(True)    

#for i in range(10):
#    wt0key, rel0key=  strainKeys(i)
#    wt0=KeysDat(wt0key)
#    ploting(wt0,'wt',i)    
   
dbase.close()   