# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 14:57:17 2015

@author: evgeniydonev
"""
import numpy as np
from pandas import ExcelWriter
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data1=pd.read_excel("data2.xlsx", 'data1')
cultures=['1','2','3']
#plt.figure()
for culture in cultures:
#IF YOU WANT TO PLOT SEPARATE TAKE AWAY THE 1 FROM THE FIGURE
    fig = plt.figure(1) #PLOTING TOGETHER
    ax = fig.add_subplot(111)
    
    ax.plot(data1['Time(min)'],data1['OD600_'+str(culture)], marker='<', markersize=16)
    ax.set_xlim([-1,max(data1['Time(min)']+60)]) 
    ax.set_ylim([-1,4])
    ax.legend(cultures,fontsize=16)
#    ax.plot(data1['Time(min)'],data1['OD600_A'])
    ax.set_yscale('log',fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    plt.ylabel('OD600_',fontsize=16)
    plt.xlabel('Time(min)',fontsize=16)
    ax.grid(True)
    fig.savefig('OD600_'+str(culture)+'.pdf', bbox_inches='tight') #save pdf figure



data2=np.array(data1)
data3=data2.T
data4=pd.DataFrame(data3)
men=data4[1:].mean()
sd=data4[1:].std()
plt.figure()
plt.errorbar(data3[0], men,yerr=sd,color='r')
plt.yscale('log')
plt.title("Mean with Std",fontsize=16)
plt.ylabel('OD600_',fontsize=16)
plt.xlabel('Time(min)',fontsize=16)
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)





     
#cycle=['r', 'g', 'b', 'y','m']
#fig1=plt.figure(1)
#
#for culture,color in zip( cultures,cycle):
#    
#    
#    data1.plot('Time(min)','OD600_'+str(culture),color=color, marker='o').set_yscale('log')
#    plt.title('Loagaritmic')
#    plt.ylabel('OD600_')
#    plt.legend(culture)
#print(data1)
#


##SAVE IN EXCEL
data=[data3[0],np.array(men),np.array(sd)]
dat=np.array(data).T
data5=pd.DataFrame(dat,columns=['Time','mean', 'std'])

writer = ExcelWriter('output.xlsx')
data5.to_excel(writer,'Sheet1')
writer.save()
   
  




