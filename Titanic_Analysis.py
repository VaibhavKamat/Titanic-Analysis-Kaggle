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
    '''Returns the percentage of a particular attribute in a dataset'''
    return np.mean(arr)*100

def get_crew_data(data):
    '''Returns the total number of crew members on board and number of crew members survived.'''
    c,s = 0,0
    for i in range(len(data)):
        
        if str(data.iloc[i]['Cabin']) != 'nan':
            c+=1
            if data.iloc[i]['Survived'] == 1:
                s+=1
    return c,s
    
def autolabel(rects,x=0.15,y=0.6):
    '''Labels the bar graphs according to the height of the bars
    '''
    for rect in rects:
        h = rect.get_height()
        plt.text(rect.get_x()+x,y*h,int(h),ha='center',va='bottom',color='white',size=12)








    
data = pd.read_csv("titanic_data.csv")# Input from the Titanic data CSV file
# Age distribution within the passenger classes (Kernel Density Estimation)     
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3)
data.Age[data.Pclass == 1].plot(kind='kde',color='blue')    
data.Age[data.Pclass == 2].plot(kind='kde',color='red')
data.Age[data.Pclass == 3].plot(kind='kde',color='orange')
plt.xlabel("Age")    
plt.title("Age Distribution (Kernel Density Estimation) within the passenger classes",size=14)
plt.legend(('1st Class', '2nd Class','3rd Class')) 
plt.show()



# Number of males and females onboard the Titanic, grouped according to the passenger class
data_by_pclass = data.groupby(['Pclass','Sex'])
males_onboard = []
females_onboard = []

for i in range(1,4):
    females_onboard.append(data_by_pclass['Survived'].count()[i][0])
    males_onboard.append(data_by_pclass['Survived'].count()[i][1])
    
width = 0.3
index = np.arange(3)
fig,ax = plt.subplots()
   
ax2 = plt.subplot2grid((3,3),(1,0),colspan=3)   
rects1 = ax2.bar(index,females_onboard,width,color='blue')
rects2 = ax2.bar(index+width,males_onboard,width,color='green')      
ax2.set_xticks(index+width)
ax2.set_xticklabels(('Class1','Class2','Class3'))
ax2.legend((rects1[0],rects2[0]),('Females','Males'),loc='best')
ax2.set_ylim(0,400)
plt.title("Number of males and females onboard the Titanic, grouped according to the passenger class",size=14)
autolabel(rects1,0.15,0)
autolabel(rects2,0.15,0.2)
plt.show()



# number of people based on port of embarkation
data_by_embark = data.groupby('Embarked')
embarked = np.array(data_by_embark.count()['Survived'])

ax3 = plt.subplot2grid((3,3),(2,0),colspan=3)
rects = ax3.barh(index,embarked,width,color='brown')
ax3.set_yticks(index+width)
ax3.set_yticklabels(('Cherbourg','Queenstown','Southampton'))
for i in range(len(embarked)):
    plt.text(embarked[i],i,embarked[i],color='blue',size=12)
plt.title("Number of people onboard Titanic based on port of Embarkation",size=14)
plt.show()
#########################################################################################################################

# Number Of People And Those Survived, Grouped By The Passenger Class
total_survived = (data['Survived']).sum()
print "Number of people survived are:%d"%(total_survived)

data_by_pclass = data.groupby('Pclass')
total = data_by_pclass['Survived'].count()
survived = data_by_pclass['Survived'].sum()
not_survived = total-survived

width = 0.3
index = np.arange(3)
fig,ax = plt.subplots()

rects1 = ax.bar(index,total,width,color='blue')
rects2 = ax.bar(index+width,survived,width,color='green')
rects3 = ax.bar(index+2*width,not_survived,width,color='red')
ax.set_xticks(index+width)
ax.set_xticklabels(('Class1','Class2','Class3'))
ax.legend((rects1[0],rects2[0],rects3[0]),('Total','Survived','Not Survived'),loc='best')
plt.title("Number Of People And Those Survived, Grouped By The Passenger Class")
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.show()

