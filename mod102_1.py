from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from random import *

#make an array

m = 12  #rows
n = 22  #cols
ambient = 25.0 #temp in degrees C
temp = np.empty(shape=(m,n))

for i in range(0,m):
    for j in range(0,n):
        temp[i,j]=ambient

#set some hot and cold spots
hot = 150   #deg C
cold = 0    #deg C
medium = 75 #deg C

#print len(temp), len(temp[0])
#make whole left side cold
for i in range(0,len(temp)):
    temp[i,0] = cold

#make whole right side hot
for i in range(0,len(temp)):
    temp[i,len(temp[0])-1] = hot

#make whole top medium
for i in range(1,len(temp[0])-1):
    temp[0,i] = medium

plt.imshow(temp, cmap='hot', interpolation='nearest')
plt.show()










