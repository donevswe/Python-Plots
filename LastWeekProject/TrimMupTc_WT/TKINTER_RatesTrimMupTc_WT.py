# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:05:35 2015

@author: ev
"""
import tkinter
#root = tkinter.Tk()
from tkinter import simpledialog
#root.withdraw()

import numpy as np
from pandas import ExcelWriter
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from polyTRim1 import polyfit

#root.withdraw()


def big(giveTime=False, x_ax=False):
    time=np.array([0, 75, 120, 180, 240, 300, 370, 420, 480, 540, 600 ])
    conc={}
    concTET=[16,8,4,2,1,0.5, 0.25, 0.125, 0]
    conc['TET']=concTET
    concMUP=[256, 128, 64, 32, 16, 8, 4, 2, 0]
    conc['MUP']=concMUP
    ant=simpledialog.askstring('Antibiotc ','write a name')
    ant=ant.upper()
    
    
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
               
    #dataFRAME=pd.DataFrame()
    #for item in sorted(dbase.keys()):
    #    dataFRAME[item]=dbase[item]
    #writer = ExcelWriter('ALLwells2.xlsx')
    #dataFRAME.to_excel(writer, 'sheet1')
    #writer.save()    
    if giveTime==True:
        n1=simpledialog.askinteger('Start','Start Time Point')
        n2=simpledialog.askinteger('Stop','Stop Time Point')
    else:
        n1=2
        n2=6
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
        ax.set_ylim([0.001,1.5])
        if x_ax==True:
            xe=simpledialog.askinteger('X_lim','set_xlim')
        else:
            xe=max(conc[str(ant)])
        ax.set_xlim([0,xe])
        
        ax.set_yscale('linear',fontsize=16)
        ax.set_xscale('linear',fontsize=16)
        ax.tick_params(axis='x', labelsize=14)
        ax.tick_params(axis='y', labelsize=14)
        plt.ylabel('Kn/K1',fontsize=16)
        plt.xlabel('Conc '+str(antib)+ ' (microM)',fontsize=16)
        ax.grid(True) 
        #fig.savefig(str(antib)+str(n1)+':'+str(n2)+'.pdf')
        return fig
        
        
    
    def ShowRate(c):
        if c=='TET':
            Kn=np.array(dataRATE['tetMEAN'])
            K1=np.array(dataRATE['tetMEAN'][8])
            KnSD=np.array(dataRATE['tetSD'])
            K1SD=np.array(dataRATE['tetSD'][8])
            figure=plotRate(Kn, K1, KnSD, K1SD, concTET, c)
        elif c=='MUP':
            Kn=np.array(dataRATE['mupMEAN'])
            K1=np.array(dataRATE['mupMEAN'][8])
            KnSD=np.array(dataRATE['mupSD'])
            K1SD=np.array(dataRATE['mupSD'][8])
            figure=plotRate(Kn, K1, KnSD, K1SD, concMUP, c)
        
        return figure
     
    ShowRate(ant)        
        
        

from tkinter import *

root = Tk()

def default():
    big()

def timePoints():
    big(giveTime=True, x_ax=False)


def X_axis():
    big(giveTime=False, x_ax=True)

def both():
    big(giveTime=True, x_ax=True)

fr1 = Frame(root)
fr2 = Frame(root)
opt = {'fill': BOTH, 'side':LEFT, 'padx': 2, 'pady': 3}
Label(text="Demo Wells Atnibiotica").pack()
Button(fr1, text='default', command=default).pack(opt)
Button(fr1, text='Give Time Points', command=timePoints).pack(opt)
Button(fr1, text='Change X_ax', command=X_axis).pack(opt)
Button(fr2, text='Personalize', command=both).pack(opt)
Button(fr2, text='Run', command=root.destroy).pack(opt)


fr1.pack()
fr2.pack()
root.mainloop()
    
    




    
    
    
    
    
    
    