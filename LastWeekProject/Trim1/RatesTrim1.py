# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:05:35 2015

@author: ev
"""

import numpy as np
from pandas import ExcelWriter
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from polyTRim1 import polyfit

time=np.array([0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660])
time=time[0:]

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

dataFRAME=pd.DataFrame()
for item in sorted(dbase.keys()):
    dataFRAME[item]=dbase[item]
writer = ExcelWriter('ALLwells1.xlsx')
dataFRAME.to_excel(writer, 'sheet1')
writer.save()               



def polynome(x,y,n, name):
    
    
    #print(y)
    ans=polyfit(x[2:6], y[2:6], n, name, c=False) 
    return ans
    
def strainRats(col):
    ratwt=[]
    ratrelA=[]
    
    for key in sorted(dbase.keys()):
        if key[1]==str(col) and int(key[0]) in [0,1,2]:
            rata1=polynome(time,np.log(dbase[key]),len(time) , 'wt'+str(key) )
            ratwt.append(rata1)
            
        elif key[1]==str(col) and int(key[0]) in [3,4,5]:
            rata=polynome(time,np.log(dbase[key]),len(time) , 'wt'+str(key) )
            ratrelA.append(rata)
    return ratwt, ratrelA
            
    
#colors=['b', 'g', 'r', 'c','m','y', 'k', 'w', 'b','g']
wtratMEN={}
relratMEN={}
wtratSD={}
relratSD={}

for i in range(10): # 10= the number of columns
    wt0key, rel0key=  strainRats(i)
    relratMEN[str(i)]=np.mean(rel0key)
    relratSD[str(i)]=np.std(rel0key)
    
    wtratMEN[str(i)]=np.mean(wt0key)
    wtratSD[str(i)]=np.std(wt0key)

WTmean=[]
RELmean=[]
WTsd=[]
RELsd=[]
for key in sorted(wtratMEN.keys()):
    men=wtratMEN[key]
    WTmean.append(men)
    
for key in sorted(relratMEN.keys()):
    men1=relratMEN[key]
    RELmean.append(men1)
    
for key in sorted(wtratSD.keys()):
    SD=wtratSD[key]
    WTsd.append(SD)
    
for key in sorted(relratSD.keys()):
    SD1=relratSD[key]
    RELsd.append(SD1)

conc=[64,32,16,8,4,2,1,0.5]
dtRAT=pd.DataFrame(index=conc)
dtRAT['wtMEN']=np.array(WTmean[:-2])
dtRAT['wtSD']=np.array(WTsd[:-2])
dtRAT['relMEN']=np.array(RELmean[:-2])
dtRAT['relSD']=np.array(RELsd[:-2])


Kn=np.array(dtRAT['wtMEN'])
K1=np.array(RELmean[-2])
KnSD=np.array(dtRAT['wtSD'])
K1SD=np.array(RELsd[-2])


#Kn=np.array(dtRAT['relMEN'])
#K1=np.array(RELmean[-2])
#KnSD=np.array(dtRAT['relSD'])
#K1SD=np.array(RELsd[-2])


def plotRate(Kn,K1,KnSD, K1SD):
    Kn1=Kn/K1
    SDkn1=(Kn/K1)*np.sqrt(((KnSD/Kn)**2)+((K1SD/K1)**2))
    
    fig=plt.figure()
    ax = fig.add_subplot(111)
    ax.errorbar(conc, Kn1,yerr=SDkn1,color='g',label='$'+str('rel')+'- %s$' % str('Kn/K1'))
    ax.legend(fontsize=16)
    #ax.set_xlim([-1,max()]) 
    ax.set_ylim([0.04,1.5])
    
    ax.set_yscale('linear',fontsize=16)
    ax.set_xscale('log',fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    plt.ylabel('Kn/K1',fontsize=16)
    plt.xlabel('Conc Trim (microM)',fontsize=16)
    ax.grid(True)   
    
plotRate(Kn,K1,KnSD, K1SD)
    
    
    
    
    
    
    
    
    
    
    