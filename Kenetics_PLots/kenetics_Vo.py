# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:52:35 2015

@author: ev
"""
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm


def fit_line_Vo(x, y, n):
    """Return slope, intercept of best fit line."""
    x1=x[0:n]
    y1=y[0:n]
    X = sm.add_constant(x1)
    model = sm.OLS(y1, X, missing='drop') # ignores entires where x or y is NaN
    fit = model.fit()
    m=fit.params[1] 
    b=fit.params[0] 
#    stderr=fit.bse # could also return stderr in each via fit.bse
    
    N = 100 # could be just 2 if you are only drawing a straight line...
    points = np.linspace(x.min(), x.max(), N)
    
    
    fig=plt.figure(1) #PLOTING TOGETHER
    
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.plot(points, m*points + b)
    
    plt.legend(['data','fitt Vo'],fontsize=16)
    
    ax.set_yscale('linear',fontsize=16)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    plt.ylabel('Abs',fontsize=16)
    plt.xlabel('Time(sec)',fontsize=16)
    ax.grid()
    plt.grid()
    plt.show()
    
    print("The Vo fitted model is:      {0:2f}*x+{1:2f} ".format(m, b))
    return m,b
   