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

time=np.array([0, 75, 120, 180, 240, 300, 370, 420, 480, 540, 600 ])


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
writer = ExcelWriter('ALLwells2.xlsx')
dataFRAME.to_excel(writer, 'sheet1')
writer.save()    

n1=2
n2=8
def polynome(x,y,n, name):
    x1=x[n1:n2]
    y1=y[n1:n2]
    #print(y)
    ans=polyfit(x1, y1, len(x1), name, c=False) 
    return ans
    
def strainRats(col):
    rateTET=[]
    rateMUP=[]
    
    for key in sorted(dbase.keys()):
        if key[1]==str(col) and int(key[0]) in [0,1,2]:
            rata1=polynome(time,np.log(dbase[key]),len(time) , 'wt'+str(key) )
            rateTET.append(rata1)
            
        elif key[1]==str(col) and int(key[0]) in [3,4,5]:
            rata=polynome(time,np.log(dbase[key]),len(time) , 'wt'+str(key) )
            rateMUP.append(rata)
    return rateTET, rateMUP
            
    
#colors=['b', 'g', 'r', 'c','m','y', 'k', 'w', 'b','g']
TETrateMEAN={}
MUPrateMEAN={}
TETrateSD={}
MUPrateSD={}


for i in range(10): # 10= the number of columns
    TETdata, MUPdata=  strainRats(i)
    TETrateMEAN[str(i)]=np.mean(TETdata)
    TETrateSD[str(i)]=np.std(TETdata)
    
    MUPrateMEAN[str(i)]=np.mean(MUPdata)
    MUPrateSD[str(i)]=np.std(MUPdata)
    


TETmean=[]
MUPmean=[]
TETsd=[]
MUPsd=[]
for key in sorted(TETrateMEAN.keys()):
    men=TETrateMEAN[key]
    TETmean.append(men)
    
for key in sorted(MUPrateMEAN.keys()):
    men1=MUPrateMEAN[key]
    MUPmean.append(men1)
    
for key in sorted(TETrateSD.keys()):
    SD=TETrateSD[key]
    TETsd.append(SD)
    
for key in sorted(MUPrateSD.keys()):
    SD1=MUPrateSD[key]
    MUPsd.append(SD1)


dataRATE=pd.DataFrame()
dataRATE['tetMEAN']=np.array(TETmean[:-1])
dataRATE['mupMEAN']=np.array(MUPmean[:-1])
dataRATE['tetSD']=np.array(TETsd[:-1])
dataRATE['mupSD']=np.array(MUPsd[:-1])

writer = ExcelWriter('DATArates.xlsx')
dataRATE.to_excel(writer, 'sheet1')
writer.save() 


def plotRate(Kn, K1, KnSD, K1SD, CONC, antib):
    Kn1=Kn/K1
    SDkn1=(Kn/K1)*np.sqrt(((KnSD/Kn)**2)+((K1SD/K1)**2))
    
    fig=plt.figure()
    ax = fig.add_subplot(111)
    ax.errorbar(CONC, Kn1,yerr=SDkn1,color='g',label='$'+str('wt')+str(antib)+'- %s$' % str('Kn/K1'))
    ax.legend(fontsize=16)
    #ax.set_xlim([-1,max()]) 
    ax.set_ylim([0.001,2])
    ax.set_xlim([0,60])
    
    ax.set_yscale('linear',fontsize=16)
    ax.set_xscale('linear',fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    plt.ylabel('Kn/K1',fontsize=16)
    plt.xlabel('Conc '+str(antib)+ ' (microM)',fontsize=16)
    ax.grid(True) 
    fig.savefig(str(antib)+str(n1)+':'+str(n2)+'.pdf')
    return Kn1, SDkn1
    

def ShowRate(c):
    if c=='TET':
        conc=[16,8,4,2,1,0.5, 0.25, 0.125, 0]
        posK1=len(conc)
        Kn=np.array(dataRATE['tetMEAN'])
        K1=np.array(dataRATE['tetMEAN'][int(posK1)-1])
        KnSD=np.array(dataRATE['tetSD'])
        K1SD=np.array(dataRATE['tetSD'][int(posK1)-1])
        KN1, SDkN1=plotRate(Kn, K1, KnSD, K1SD, conc, c)
    elif c=='MUP':
        conc=[256, 128, 64, 32, 16, 8, 4, 2, 0]
        posK1=len(conc)
        Kn=np.array(dataRATE['mupMEAN'])
        K1=np.array(dataRATE['mupMEAN'][int(posK1)-1])
        KnSD=np.array(dataRATE['mupSD'])
        K1SD=np.array(dataRATE['mupSD'][int(posK1)-1])
        KN1, SDkN1=plotRate(Kn, K1, KnSD, K1SD, conc, c)
    return KN1, SDkN1    
A,B=ShowRate('MUP')        
        
        



#plotRate(Kn,K1,KnSD, K1SD,conc,'MUP' )
##plotRate(Kn,K1,KnSD, K1SD,'TET' )
    

    
    
    
    
    
    
    
    
    