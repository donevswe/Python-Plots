# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:10:32 2015

@author: ev
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import seaborn as sns

# Let's create a function to model and create data

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
    """If c then we have 3 gradig polyome"""
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


# Check
    
    
    
    
    
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
    #print( popt )
    #fig.savefig('scipy_311_ex2.pdf', bbox_inches='tight')
    return popt


if __name__ == "__main__":
    import pandas as pd
    
#    for i in range(1,8):
#        file='/home/ev/Documents/Kenetics_PLots/Sample-'+str(i)+'.xlsx'
#        data1 = pd.read_excel(file)
#        x=data1['Time(sec)']
#        y=data1['Abs']
#        fun=polyfit(x[10:], y[10:], 200,'wt', c='poly2')



    x1=np.linspace(1000, 200000, num=20)
#    y0=3*x**2+6*x+6
#    y1=3*x+6
#    y2=3*np.exp(x)  
#    y4=3*np.log(6*x) 
    file='lab1_data.xls'
    data1 = pd.read_excel(file)
    x=data1['n']
    y=data1['tid']
    
#    x=np.linspace(1,10,10)
#    y=[3.08,12.05,27.12,48.22,75.41,108.43,147.3,192.43,243.44,300.13]
    
    fun=polyfit(x, y, 200,'f(n)', c='poly2')
    def myfun(x1):
        ansi=(fun[0]*x1**2)+fun[1]*x1+fun[2]
        return ansi
    polyfit(x1,myfun(x1),200,'myfun',c='poly2' )
    """" NÄR MAN HAR IENTIFIRAT IF IT IS POLY1...2 ELLER ANNAT
    DECITE A POLYNOME(y1) AND the kvot y/y1 which should go to aproximately a constant value
    DO THE FLLOWING"""
    y1=x**2
    kvotY=y/y1
    
    fun1=polyfit(x,kvotY,200,'kvotY',c='poly1' )
   
    
    
    
    
    
