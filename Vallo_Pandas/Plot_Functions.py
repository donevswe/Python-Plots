# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:26:08 2015

@author: ev
"""

from numpy import *
import matplotlib.pyplot as plt
"""I define a couple of functions (a,b,c,d) an then plot them"""


x = arange(0,10,0.2)
a = x
b = x*3
c = x*x
d = x*log(x)
e=2**x
la = plt.plot(x,a,'b-',label='x')
lb = plt.plot(x,b,'r--',label='3x')
lc = plt.plot(x,c,'gx',label='x²')
ld = plt.plot(x,d,'y-', linewidth = 1,label='xlog(x)')
le=plt.plot(x,e,'r-', linewidth = 1,label='2^n')


ll = plt.legend(loc='upper left')
lx = plt.xlabel('xaxis')
ly = plt.ylabel('yaxis')
plt.grid()


plt.show()