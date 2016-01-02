# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 14:57:17 2015

@author: evgeniydonev
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data1=pd.read_excel("data1.xlsx", 'data1')
cultures=['WT','A','B','C','D']
#plt.figure()
for culture in cultures:
#IF YOU WANT TO PLOT SEPARATE TAKE AWAY THE 1 FROM THE FIGURE
    fig = plt.figure(1) #PLOTING TOGETHER
    ax = fig.add_subplot(111)
    
    ax.plot(data1['Time(min)'],data1['OD600_'+str(culture)])
    ax.legend(cultures,fontsize=16)
#    ax.plot(data1['Time(min)'],data1['OD600_A'])
    ax.set_yscale('log',fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    plt.ylabel('some numbers',fontsize=16)
    plt.xlabel('Time(min)',fontsize=16)
    ax.grid()


cultures=['WT','A','B','C','D']        
cycle=['r', 'g', 'b', 'y','m']
fig1=plt.figure(1)

for culture,color in zip( cultures,cycle):
    
    
    data1.plot('Time(min)','OD600_'+str(culture),color=color).set_yscale('log')
    plt.title('Loagaritmic')
    plt.ylabel('OD600_')
    plt.legend(culture)
print(data1)


    
  




