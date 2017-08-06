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

def read_data(filename):
    '''Reading data from a CSV file using pure python without using pandas.
    '''
    with open(filename,'rb') as f:
        reader=unicodecsv.DictReader(f)
        data=list(reader)
    for datum in data: 
       
        datum['Survived']=parse_int(datum['Survived'])
        datum['Age']=parse_int(float(datum['Age']))
        datum['SibSp']=parse_int(datum['SibSp'])
        datum['Parch']=parse_int(datum['Parch'])
        datum['Pclass']=parse_int(datum['Pclass'])
        datum['Parch']=parse_float(datum['Parch'])
    return data

def parse_int(item):
    '''Parsing string input from a CSV file into integer
    '''
    if item=='':
        return None
    else:
        return int(item)

def parse_float(item):
    '''Parsing string input from a CSV file into float
    '''
    if item=='':
      	return None
    else:
	    return float(item)

def group_data(data,key_name):
    '''Grouping data based on a key_field(column) without pandas
    '''
    grouped_data=defaultdict(list)
    for data_point in data:
        key=data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data

def sum_grouped_items(grouped_data,field_name): 
    '''Finds the sum of the various attributes of a grouped dataset.
    '''
    summed_data={}                              
    for key,data_points in grouped_data.items():
        total=0
        for data_point in data_points:
            total+=data_point[field_name]
        summed_data[key]=total
    return summed_data
    
def group_by_age(data):
    '''Grouping a data set based on age groups the individual data point falls into
       Age groups are 0-12,13-17,18-39,40-59,60 and above.'''
    grouped_data=defaultdict(list)
    for datum in data:
        if (datum['Age'] >=0 and datum['Age']<13):
            grouped_data['under_13'].append(datum)
        if (datum['Age'] >=13 and datum['Age']<18):
            grouped_data['under_18'].append(datum)	
        if (datum['Age']>=18 and datum['Age']<40):
            grouped_data['under_40'].append(datum)
        if (datum['Age']>=40 and datum['Age']<60):
            grouped_data['under_60'].append(datum)
        if (datum['Age']>=60):
            grouped_data['above_60'].append(datum)    
    return grouped_data    

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
        plt.text(rect.get_x()+0.23,1.05*h,int(h),ha='center',va='bottom')
    
    
        
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

autolabel(rects1)
autolabel(rects2)
plt.show()
