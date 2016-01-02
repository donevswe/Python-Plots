# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 15:13:36 2015

@author: ev

"""

import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



data=pd.read_excel('allwells.xlsx','1')  # have a look at the data first
print('Here it comes a column 00')
print(data['00']) # get a whole column ;see the data column '00'


print('=='*20)
print('Here it comes row with index 75')
print(data.loc[75,:]) # get a whole row ; see the data row with index 75

print('=='*20)
print('Here it comes rows with index=75 to the end, columns 00-02')
print(data.loc[75:,'00':'02'])  # get row with index 75 to the end; colmuns from '00' to '02'

print('=='*20)
print('Here it comes row with index=75:300, columns 00-02')
print(data.loc[75:300,'00':'02'])  #here you cut row with index 75 to 300; columns from '00' to '02'




"""Let us imagie that we have three replicates column 00 to 02 and we want to plot means with std"""
print('=='*20)
print('\nHere comes your replicates')
myreplica=data.loc[:,'00':'02']
print(myreplica)

print('=='*20)
print('\nHere comes the Stats of your replicates column bu column')
print(myreplica.describe())

"""Get the rows numbers"""
print('=='*20)
print('\nHere comes only the row indexes')
print(myreplica.index.get_values())
indexes=myreplica.index.get_values()  # I am giving them a variable indexes since it will be my x axis on the plot

"""As I told you if you want to make manipultion we convert the data to array"""
myreplica=np.array(myreplica)


"""If you want to check them one by one try """

print('=='*20)
print('\nHere comes your replicate nr.1')
print(myreplica.T[0])  # I am transposing the matrix first .T -symbol means transpose

print('=='*20)
print('\nHere comes your replicate nr.2')
print(myreplica.T[1])  # I am transposing the matrix first .T -symbol means transpose

print('=='*20)
print('\nHere comes your replicate nr.3')
print(myreplica.T[2])  # I am transposing the matrix first .T -symbol means transpose

"""Let us get the means for each end every timepoint"""

means=[None]*len(myreplica)  # creating an empty list for the means with the length of my timepoints indexes
std=[None]*len(myreplica)    # creating an empty list  for the std
for i in range(len(myreplica)):
    means[i]=np.mean(myreplica[i])   # numpy is calculating the means and std for every row and then add it to the list
    std[i]=np.std(myreplica[i])
    


"""Lets plot them"""

fig=plt.figure()
ax = fig.add_subplot(221)

#color='g',label='$'+str('wt')+str(antib)+'- %s$' % str('Kn/K1')
ax.errorbar(indexes, means, std, color='g',label='Your replicates' ,linestyle='-', marker='^')
ax.legend(fontsize=16)

#ax.set_ylim([0,10])
ax.set_xlim([0,700])

ax.set_yscale('linear',fontsize=16)
ax.set_xscale('linear',fontsize=16)
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
plt.ylabel('My REplicates',fontsize=16)
plt.xlabel('Time points',fontsize=16)
ax.grid(True) 


ax = fig.add_subplot(222)

#color='g',label='$'+str('wt')+str(antib)+'- %s$' % str('Kn/K1')
ax.errorbar(indexes, means, std, color='g',label='Your replicates' ,linestyle='-', marker='^')
ax.legend(fontsize=16)

#ax.set_ylim([0,10])
ax.set_xlim([0,700])

ax.set_yscale('linear',fontsize=16)
ax.set_xscale('linear',fontsize=16)
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
plt.ylabel('My REplicates',fontsize=16)
plt.xlabel('Time points',fontsize=16)
ax.grid(True) 
plt.show()
plt.show()