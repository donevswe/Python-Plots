# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 22:48:13 2015

@author: ev
"""
import pandas as pd
from kenetics_Vo import fit_line_Vo
from Regresison1 import polyfit
import seaborn as sns


for i in range(1,8):
    file='/home/ev/Documents/Kenetics_PLots/Sample-'+str(i)+'.xlsx'
    
    
    
    data1 = pd.read_excel(file)
    x=data1['Time(sec)']
    y=data1['Abs']
    
    
    m,b=fit_line_Vo(x,y,10)
    
    func=polyfit(x, y, 300)
    print('='*60)
    
    
    
    
