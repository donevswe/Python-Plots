# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:46:42 2015

@author: vvarik
"""

""" One of my first scripts, might be that not all the following needs to 
be imported"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import *

column_labels = list('BCDEFG')
row_labels = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
data = pd.read_excel('output'+str(10)+'.xlsx', 'Sheet1')
fig, ax = plt.subplots()
heatmap = ax.pcolor(data, vmin=0.03, vmax=0.3) #, cmap=cm.YlOrRd)

""" vmin, vmax will set the range for heatmap, without it, maximal range 
will be used and in case of several plots, this might vary, resulting in 
badly comparable coloring. Colour scheme can be defined by 
cmap=cm.NameofthecolourScheme """ 

# put the major ticks at the middle of each cell, notice "reverse" use of dimension
ax.set_yticks(np.arange(data.shape[0])+0.5, minor=False)
ax.set_xticks(np.arange(data.shape[1])+0.5, minor=False)


ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(column_labels, minor=False)

ax.invert_yaxis()
ax.xaxis.tick_top()

cbar = plt.colorbar(heatmap)

#fig.savefig("4-7h.pdf")
#plt.show()




