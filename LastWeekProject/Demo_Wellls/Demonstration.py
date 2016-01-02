# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:05:56 2015

@author: ev
"""
# The following five lines import some necessary pthon modiles
import numpy as np
from pandas import ExcelWriter
#import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


time=np.array([0, 75, 120, 180, 240, 300, 370, 420, 480, 540, 600 ])  # here we define the timepoints we have collected our data


#Create the table that will gather our well's values. WE OPEN THE FIRST ZERO TIME PINT MEASUREMENT EXCEL SHEET
dbase={}   # WE create a dictionary that will collect our data. Dictionery is as table we have a key and a data conected to that key
data=pd.read_excel('output'+str(0)+'.xlsx', 'Sheet1') # opens the excel sheet from the first the zero time point
data=np.array(data)       # converts it to array, so we can manipualte the data easier
for i in range(len(data)):       # the numbers of rows. Goes though the rows
    for ii in range(len(data[i])):    # the numbers. For every row goes through the columns
        x=str(i)+str(ii)  # we create a temporary variable that has a value x= rowNUm colNUm, for example x= '34' means row 3 column 4
        dat=[]  # a list that will contain the first value of the cell. It will be cleaned every time the loop runs the newxt value
        dat.append(data[i][ii])  # we put the value of the well to the list
        dbase[x]=dat  # the list is put to the table. For example dabse['20']= some OD value   
        
# then we go through the rest of the excell time points and collect them
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
           
           
def Replicas(col):
    Strain1_replicates=[]
    Strain2_replicates=[]
    
    for key in sorted(dbase.keys()):
        if int(key[0]) in [0,1,2] and key[1]==str(col):  # if the key contains x= rowNUm=[1,2,3]  and  columnNr = col _argument
            Strain1_replicates.append(dbase[key])       # then we know taht these are replicates
            
            
        elif int(key[0]) in [3,4,5] and key[1]==str(col):   # if the key contains x= rowNUm=[1,2,3]  and  columnNr = col _argument
            Strain2_replicates.append(dbase[key])               # then we know taht these are replicates
            
    return np.array(Strain1_replicates), np.array(Strain2_replicates)




def ReplicaStats(myreplica):
    """Let us get the means for each end every timepoint"""

    means=[None]*len(myreplica)  # creating an empty list for the means with the length of my timepoints indexes
    std=[None]*len(myreplica)    # creating an empty list  for the std
    for i in range(len(myreplica)):
        means[i]=np.mean(myreplica[i])   # numpy is calculating the means and std for every row and then add it to the list
        std[i]=np.std(myreplica[i])
    
    return means, std



def PlotMyreplica(timePoints, means, std, replicaNr, col):
    """Lets plot the means with std"""
    
    fig=plt.figure()
    ax = fig.add_subplot(111)
    
    ax.errorbar(timePoints, means, std, color='g',label='Replicate'+str(replicaNr)+ ' Column'+str(col) ,linestyle='-', marker='^')
    ax.legend(fontsize=16)
    
    ax.set_ylim([0.03,0.8])
    ax.set_xlim([0,700])
    
    ax.set_yscale('log',fontsize=16)
    ax.set_xscale('linear',fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    plt.ylabel('My REplicates',fontsize=16)
    plt.xlabel('Time points',fontsize=16)
    ax.grid(True) 
    #fig.savefig('Replicate'+str(replicaNr)+ ' Column'+str(col)+'.pdf')
    plt.show()



def Display(replica,Nr, column):      # WE just put Replicastats and PLotMyreplica together
    mean, Std = ReplicaStats(replica)
    PlotMyreplica(time, mean, Std, Nr, column)    



def runColumn(n):# put a number of the column you want to see. Start with zero
    Column=n    
    ReplicaNr=1  # we start allways with replica 1
    for replic in Replicas(Column):    # see the function Replicas above on line 49 if you are getting lost
                                       
        Display(replic.T,ReplicaNr, Column)
        ReplicaNr +=1


for col in range(10):
    runColumn(col)
#runColumn(0)







