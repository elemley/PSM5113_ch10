from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *
from random import *

#make an array

m = 10  #rows
n = 10  #cols
ambient = 25.0 #temp in degrees C
temp = np.empty(shape=(m,n))

#print temp

for i in range(0,m):
    for j in range(0,n):
        temp[i,j]=ambient

#print temp

#set some hot and cold spots
hot = 150   #deg C
cold = 0    #deg C

hot_list = [(1,3),(1,4)]
cold_list = [(0,0),(3,5),(7,1)]

temp[hot_list[0]] = hot
temp[hot_list[1]] = hot

temp[cold_list[0]] = cold
temp[cold_list[1]] = cold
temp[cold_list[2]] = cold

#print temp

plt.imshow(temp, cmap='hot',interpolation='nearest')
#, interpolation='nearest')
plt.show()


"""
fig1=plt.figure()
plt.axes()

rectangle = plt.Rectangle((0,0),1,1,fc='r')
plt.gca().add_patch(rectangle)

plt.axis('equal')
plt.show()
"""
















