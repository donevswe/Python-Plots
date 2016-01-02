# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 00:20:35 2015

@author: ev
"""
import pandas as pd


file='Substrate_conc_vs_Vo.xlsx'

data1 = pd.read_excel(file)
sub=data1['Ethanol(M)']
Vo=data1['Vo(nmol/s)']
print(data1)


import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm



x1=sub
y1=Vo
fig=plt.figure() #PLOTING TOGETHER

ax = fig.add_subplot(111)
ax.plot(x1, y1)

plt.legend(['Vmax','fitt Vo'],fontsize=16)

ax.set_yscale('linear',fontsize=16)
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
plt.ylabel('Vo',fontsize=16)
plt.xlabel('Substrate(M)',fontsize=16)
ax.grid()
plt.show()


x=1/x1
y=1/y1

X = sm.add_constant(x)
model = sm.OLS(y, X, missing='drop') # ignores entires where x or y is NaN
fit = model.fit()
m=fit.params[1] 
b=fit.params[0] 
#    stderr=fit.bse # could also return stderr in each via fit.bse

N = 2 # could be just 2 if you are only drawing a straight line...
points = np.linspace(x.min(), x.max(), N)



fig=plt.figure() #PLOTING TOGETHER

ax = fig.add_subplot(111)
ax.plot(x, y,'ro')
ax.plot(points, m*points + b)

#plt.legend(['Vmax','fitt Vo'],fontsize=16)

ax.set_yscale('linear',fontsize=16)
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
plt.ylabel('1/Vo',fontsize=16)
plt.xlabel('1/Substrate(M)',fontsize=16)
ax.grid()
plt.show()

print("The fitted model is:      {0:2f}*x+{1:2f} ".format(m, b))





