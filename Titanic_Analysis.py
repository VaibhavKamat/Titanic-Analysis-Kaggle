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
    
def autolabel(rects,x=0.15,y=0.6,color='white',size=12):
    '''Labels the bar graphs according to the height of the bars
    '''
    for rect in rects:
        h = rect.get_height()
        plt.text(rect.get_x()+x,y*h,int(h),ha='center',va='bottom',color=color,size=size)








    
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

# The data type of the crew members features is a string (with cabin numbers) or float with nan value
# The number of nan values is 204, which is the number of crew members in the data
c= 0
for datum in data['Cabin']:
    if type(datum)!=float:
        c+=1
print '\n \nThe number of crew members in the data is %d \n\n'%(c)       
#########################################################################################################################

# Number Of People And Those Survived, Grouped By The Passenger Class
total_survived = (data['Survived']).sum()
print "Number of people survived are:%d"%(total_survived)

data_by_pclass = data.groupby('Pclass')
total = data_by_pclass['Survived'].count()
survived = data_by_pclass['Survived'].sum()
not_survived = total-survived

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




# Number of males and females who survived, grouped according to the passenger class
data_by_pclass = data.groupby(['Pclass','Sex'])
males_onboard = []
females_onboard = []

for i in range(1,4):
    females_onboard.append(data_by_pclass['Survived'].sum()[i][0])
    males_onboard.append(data_by_pclass['Survived'].sum()[i][1])
    
fig,ax = plt.subplots()
rects1 = ax.bar(index,females_onboard,width,color='brown')
rects2 = ax.bar(index+width,males_onboard,width,color='orange')      
ax.set_xticks(index+width)
ax.set_xticklabels(('Class1','Class2','Class3'))
ax.legend((rects1[0],rects2[0]),('Females','Males'),loc='best')
plt.title("Number of males and females who survived, grouped according to the passenger class",size=14)
autolabel(rects1)
autolabel(rects2)
plt.show()
print """This suggests the number of males survived in all three classes where lower than that of females, \
which means women were given more preference, in the rescue operations."""



#Number of people and those survived, according to the age groups
data_by_age=data.groupby(pd.cut(data['Age'],[0,12,18,40,60,100]))
total_by_age = np.array(data_by_age['Survived'].count())
survived_by_age = np.array(data_by_age['Survived'].sum())

index = np.arange(5)
fig,ax = plt.subplots()
rects1 = ax.bar(index,total_by_age,width,color='blue')
rects2 = ax.bar(index+width,survived_by_age,width,color='green')
ax.set_xticks(index+width)
ax.set_xticklabels(('0-12','12-18','18-40','40-60','60-100'))
ax.legend((rects1[0],rects2[0]),('Total','Survived'),loc='best')
plt.title("Total number of people and those survived, according to the age groups",size=14)
autolabel(rects1,0.2,1,color='black',size=15)
autolabel(rects2,0.2,1,color='black',size=15)
plt.show()



# displaying how many survived in different passenger classes, among men and women
data_by_pclass = data.groupby(['Pclass','Sex'])
males_onboard = []
females_onboard = []
males_survived = []
females_survived = []

for i in range(1,4):
    females_onboard.append(data_by_pclass['Survived'].count()[i][0])
    females_survived.append(data_by_pclass['Survived'].sum()[i][0])
    males_onboard.append(data_by_pclass['Survived'].count()[i][1])
    males_survived.append(data_by_pclass['Survived'].sum()[i][0])
    
    
print males_onboard
print males_survived
print females_onboard
print females_survived

index = np.arange(3)
ax2 = plt.subplot2grid((2,2),(0,0),colspan=2)   
rects1 = ax2.bar(index,females_onboard,width,color='blue')
rects2 = ax2.bar(index+width,females_survived,width,color='green')      
ax2.set_xticks(index+width)
ax2.set_xticklabels(('Class1','Class2','Class3'))
ax2.legend((rects1[0],rects2[0]),('Total','Survived'),loc='best')
plt.title("Number of females onboard the Titanic and those survived, grouped according to the passenger \
class",size=14)
autolabel(rects1,0.15,0.3)
autolabel(rects2,0.15,0.2)
plt.show()


ax2 = plt.subplot2grid((2,2),(0,0),colspan=2)   
rects1 = ax2.bar(index,males_onboard,width,color='blue')
rects2 = ax2.bar(index+width,males_survived,width,color='green')      
ax2.set_xticks(index+width)
ax2.set_xticklabels(('Class1','Class2','Class3'))
ax2.legend((rects1[0],rects2[0]),('Total','Survived'),loc='best')
plt.title("Number of males onboard the Titanic and those survived, grouped according to the passenger \
class",size=14)
ax2.set_ylim(0,400)
autolabel(rects1,0.15,0.3)
autolabel(rects2,0.15,0.2)
plt.show()