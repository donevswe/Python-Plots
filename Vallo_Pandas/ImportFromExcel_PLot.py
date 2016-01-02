# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:01:23 2015

@author: ev
"""

from numpy import*   # on the next three lines importing the packages we usually need
import pandas as pd
import matplotlib.pylab as plt

df=pd.read_excel('winequality-red.xls')

fig = plt.figure(1)


plt.scatter(df['alcohol'], df['quality'])  # scatter plot two avriables against eachother
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.title('Alcohol Against Quality')
plt.show()


fig=plt.figure(2)
plt.plot(arange(0,8), df['quality'][0:8])  # plot to a number of rows in your data
plt.xlabel('The first Eight Wines')
plt.ylabel('Quality')
plt.title('ALCOHOL Quality to the first Eight Wines')
plt.show()

"""If you would like to get all statistics for a certain column see next"""


print(df['alcohol'].describe()) # THIS GIVES YOU ALL STATS TO COLUMN 'alcohol'

stat=df['alcohol'].describe()


count=stat[0]
std=stat[1]
min=stat[2]
max=stat[7]

print('\ncount: {0}, std: {1}, min: {2}, max: {3}'. format(count,std,min,max))



