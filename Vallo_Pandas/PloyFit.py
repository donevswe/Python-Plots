# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:41:41 2015

@author: ev
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import seaborn as sns

# Let's create a functions that we could fit to

def Exp(x, a, b):
    return a*np.exp(b*x)

def poly1(x, a, b):
    return a*x+b

def poly2(x, a, b, c):
    return a*x**2+b*x+c        

def poly3(x, a, b, c, d):
    return a*x**3+b*x**2+c*x+d

def Log(x,a,b):
    return a*np.log(b*x)

def polyfit(x, yn, n,name, c='poly1'):
    """arguments, x-axis, y-axis, n= how many values of the data will be iin the fit, name of the legend, c= function of the fit"""
    if c=='poly2':
        popt, pcov = curve_fit(poly2, x[:n], yn[:n])
        ym = poly2(x, popt[0], popt[1], popt[2])
        print("The Vo fitted model is:      {0:2f}*x²+{1:2f}*x+{2:2f} ".format(popt[0], popt[1], popt[2]))
    #Otherwise tw gradig ploynome
    elif c=='poly1' :
        popt, pcov = curve_fit(poly1, x[:n], yn[:n])
        ym = poly1(x, popt[0], popt[1])
        print("The rate fitted model is:  {1:2f}*x+{2:2f} ".format(name,popt[0], popt[1]))
        
    if c=='poly3':
        popt, pcov = curve_fit(poly3, x[:n], yn[:n])
        ym = poly3(x, popt[0], popt[1], popt[2], popt[3])
        print("The Vo fitted model is:      {0:2f}*x³+{1:2f}*x²+{2:2f}*x+{3:2f}".format(popt[0], popt[1], popt[2], popt[3]))  
        
    elif c=='exp':
        popt, pcov = curve_fit(Exp, x[:n], yn[:n])
        ym = Exp(x, popt[0], popt[1])
        print("The rate fitted model is:  {1:2f}*Exp({2:2f}*x) ".format(name,popt[0], popt[1]))
    
    elif c=='log':
        popt, pcov = curve_fit(Log, x[:n], yn[:n])
        ym = Log(x, popt[0], popt[1])
        print("The rate fitted model is:  {1:2f}*Exp({2:2f}*x) ".format(name,popt[0], popt[1]))
    #popt returns the best fit values for parameters of the given model (func)
    
    
    
    
    
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    #ax.plot(x, y, c='k', label='Function')
    ax.scatter(x, yn, color = 'r', marker = 'x')
    ax.plot(x, ym, color = 'g')
    #ax.set_ylim([0.0,4.000000e-09])
    #ax.set_xlim([-1,300])
    
    plt.legend(['fitted Model',str(name)],fontsize=16,loc='upper left')
    
    ax.set_yscale('linear',fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    plt.ylabel('Time',fontsize=16)
    plt.xlabel('Problem size (n)',fontsize=16)
    ax.grid()
    plt.grid()
    plt.show()
    #fig.savefig('scipy_311_ex2.pdf', bbox_inches='tight')
    return popt


if __name__ == "__main__":
    import pandas as pd

    file='ALLwells1.xlsx'    # have a look att this file in the map
    data1 = pd.read_excel(file)
    sample00=data1['00']   # I extract the first column and then fit it bellow
    

    """In the function polyfit the 
    first argument is the x axis 'np.arange(len(sample00)) = 0,1,2,3....len(samle00)'
    
    second argument is the y-axes = sample00
    
    third argument you can adjust how many of the values will partcipate in the fit . TRy to change 0,1,2.... len(sample00)
    
    fourth argument is the 'legend' on the plot
    
    fifth argument you can choose what functions to fit first (poly1), second(poly2), third(poly3) , exp(exp) or Log(log). Try poly1, poly2, poly3
    
    it gives you also the fitted function on top of the plot in the console
    """

    
    fun1=polyfit(np.arange(len(sample00)),sample00,11,'sample00',c='poly1' )