# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:22:11 2015

@author: ev
"""

import numpy as np
from pandas import ExcelWriter
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def createTemplate(m):
    df3 = pd.DataFrame(np.random.randn(6,10 ),index=[ 'b', 'c', 'd', 'e','f','g'], columns=[2,3,4,5,6,7,8,9,10,11])
    writer = ExcelWriter('output'+str(m)+'.xlsx')
    df3.to_excel(writer,'Sheet1')
    writer.save()    



def startShelve(data):
    import shelve
    dbase = shelve.open("mydbase") 
    # This is the limit for creation. After the fist time comment it
        
    data=np.array(data)
    for i in range(len(data)):
        for ii in range(len(data[i])):
   
            x='dat'+str(i)+str(ii)
            dat=[]
            dat.append(data[i][ii])
            dbase[x]=dat
    dbase.close()


    
def addToShelve(m):
    data=pd.read_excel('output'+str(m)+'.xlsx', 'Sheet1')
    import shelve
    dbase = shelve.open("mydbase")
    data=np.array(data)
    for i in range(len(data)):
        for ii in range(len(data[i])):
   
            x='dat'+str(i)+str(ii)
            temp=dbase[x]
            temp.append(data[i][ii])      # mutates the copy
            dbase[x] = temp 
    dbase.close()




#for i in range(0,9):
#    createTemplate(i)   

data1=pd.read_excel("output0.xlsx", 'Sheet1') 
#startShelve(data1) 

#for i in range(1,9):
#    addToShelve(i)






#import shelve
#dbase = shelve.open("mydbase")
##dbase.close()
###
####


#import shelve
#dbase = shelve.open("mydbase")
#time=[0,60,120,120,180,240,300,360,420]
##
#for culture in sorted(dbase):
#    print(culture)
##IF YOU WANT TO PLOT SEPARATE TAKE AWAY THE 1 FROM THE FIGURE
#    fig = plt.figure() #PLOTING TOGETHER
#    ax = fig.add_subplot(111)
#    
#    ax.plot(time,dbase[culture], marker='<', markersize=10,label='$Cell- %s$' % culture[3:])
#    ax.legend(fontsize=16)
#    ax.set_xlim([-1,max(time)+100]) 
#    ax.set_ylim([-5,4])
##    ax.legend(culture[3:],fontsize=16)
##    ax.plot(data1['Time(min)'],data1['OD600_A'])
#    ax.set_yscale('linear',fontsize=16)
#    ax.tick_params(axis='x', labelsize=14)
#    ax.tick_params(axis='y', labelsize=14)
#    plt.ylabel('OD600_',fontsize=16)
#    plt.xlabel('Time(min)',fontsize=16)
#    ax.grid(True)
###    #fig.savefig('OD600_'+str(culture)+'.pdf', bbox_inches='tight') #save    
#dbase.close()   
#    


  

