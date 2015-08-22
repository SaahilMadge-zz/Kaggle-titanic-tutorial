
# coding: utf-8

# In[1]:

import csv as csv
import numpy as np


# In[4]:

# Open up the csv file in to a Python object
csv_file = csv.reader(open('train.csv', 'rb'))


# In[5]:

header = csv_file.next()
print header


# In[6]:

data = []
for row in csv_file:
    data.append(row)
data = np.array(data)
print data[:5]


# In[8]:

print data[0]
print data[-1]
print data[0,3]


# In[12]:

number_passengers = np.size(data[0::,1].astype(float))
number_survived = np.sum(data[0::,1].astype(float))
proportion_survivors = number_passengers / number_survived

print number_passengers
print number_survived
print proportion_survivors


# In[13]:

femaleStats = data[0::,4] == 'female'
maleStats = data[0::,4] != 'female'


# In[16]:

womenOnboard = data[femaleStats, 1].astype(np.float)
menOnboard = data[maleStats, 1].astype(np.float)


# In[18]:

femaleProportion = np.sum(womenOnboard) / np.size(womenOnboard)
maleProportion = np.sum(menOnboard) / np.size(menOnboard)

print femaleProportion
print maleProportion


# In[ ]:



