# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 19:06:38 2016

@author: Vaibhav
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import unicodecsv
from collections import defaultdict

def percentage(arr):
    '''Returns the percentage of a particular attribute in a dataset
    '''
    return np.mean(arr)*100

def get_crew_data(data):
    '''Returns the total number of crew members on board and number of crew members survived.
    '''
    c,s=0,0
    for i in range(len(data)):
        
        if str(data.iloc[i]['Cabin'])!='nan':
            c+=1
            if data.iloc[i]['Survived']==1:
                s+=1
    return c,s
    
def autolabel(rects):
    '''Labels the bar graphs according to the height of the bars
    '''
    for rect in rects:
        h=rect.get_height()
        plt.text(rect.get_x()+0.15,0.6*h,int(h),ha='center',va='bottom',color='white',size=12)
    
    
        
data = pd.read_csv(r"E:\Udacity\Data Analysis\Project\titanic_data.csv")
data.Age[data.Pclass == 1].plot(kind='kde')    
data.Age[data.Pclass == 2].plot(kind='kde')
data.Age[data.Pclass == 3].plot(kind='kde')
plt.xlabel("Age")    
plt.title("Age Distribution (Kernel Density Estimation) Within Classes")
plt.legend(('1st Class', '2nd Class','3rd Class')) 
plt.show()


#############################################################################################
total_survived=(data['Survived']).sum()
print "Number of people survived are:%d"%(total_survived)

data_by_pclass=data.groupby('Pclass')
total = data_by_pclass['Survived'].count()
survived = data_by_pclass['Survived'].sum()
not_survived = total-survived

width=0.3
index=np.arange(3)
fig,ax=plt.subplots()
colour=[]
rects1=ax.bar(index,total,width,color='blue')
rects2=ax.bar(index+width,survived,width,color='green')
rects3=ax.bar(index+2*width,not_survived,width,color='red')
ax.set_xticks(index+width)
ax.set_xticklabels(('Class1','Class2','Class3'))
ax.legend((rects1[0],rects2[0],rects3[0]),('Total','Survived','Not Survived'),loc='best')
plt.title("Number Of People And Those Survived, Grouped By The Passenger Class")
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.show()
