import pylab as plt
import numpy as np 
import random as rd



def Clock(min=0,max=1,f=5):
    t = np.array([i for i in np.arange(min,max,1/(f*3))])
    return t,np.array([i%2 for i in range(min,len(t))])
fre = 3
t,clk = Clock(f=fre)
