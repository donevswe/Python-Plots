# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:10:32 2015

@author: ev
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import seaborn as sns
#x = np.array([0.15,2.3,3.15,4.85,6.25,7.95])
#yn = np.array([4.79867,4.49013,4.2243,3.47313,2.66674,1.51909])

# Let's create a function to model and create data

#def func1(x, a, b):
#    return a*np.exp(b*x)

def func(x, a, b, c):
    return a*x**2+b*x+c

def func1(x, a, b):
    return a*x+b
        


def polyfit(x, yn, n,name, c=False):
    """If c then we have 3 gradig polyome"""
    if c:
        popt, pcov = curve_fit(func, x[:n], yn[:n])
        ym = func(x, popt[0], popt[1], popt[2])
        print("The Vo fitted model is:      {0:2f}*x²+{1:2f}*x+{2:2f} ".format(popt[0], popt[1], popt[2]))
    #Otherwise tw gradig ploynome
    else:
        popt, pcov = curve_fit(func1, x[:n], yn[:n])
        ym = func1(x, popt[0], popt[1])
        print("The rate fitted model for Ln(mean({0}))= {1:2f}*x+{2:2f} ".format(name,popt[0], popt[1]))
    
    #popt returns the best fit values for parameters of the given model (func)
    
    
    
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.plot(x, y, c='k', label='Function')
    ax.scatter(x, yn, color = 'r', marker = 'x')
    ax.plot(x, ym, color = 'g')
    
    
    plt.legend(['fitted Model',str(name)],fontsize=16,loc='upper left')
    
    ax.set_yscale('linear',fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    plt.ylabel('Ln(OD600_)',fontsize=16)
    plt.xlabel('Time(sec)',fontsize=16)
    ax.grid()
    plt.grid()
    plt.show()
    #print( popt )
    fig.savefig('scipy_311_ex2.pdf', bbox_inches='tight')
    return popt


if __name__ == "__main__":
    import pandas as pd
    
    for i in range(1,8):
        file='/home/ev/Documents/Kenetics_PLots/Sample-'+str(i)+'.xlsx'
        data1 = pd.read_excel(file)
        x=data1['Time(sec)']
        y=data1['Abs']
        
        fun=polyfit(x, y, 300,'wt', c=False)