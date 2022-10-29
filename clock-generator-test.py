import pylab as plt
import numpy as np 
import random as rd



def Clock(min=0,max=1,f=5):
    t = np.array([i for i in np.arange(min,max,1/(f*3))])
    return t,np.array([i%2 for i in range(min,len(t))])
fre = 3
t,clk = Clock(f=fre)

fig, ax= plt.subplots(3,1,sharex='col', figsize=(21,25))
ax[0].step(Clock(f=5)[0],Clock(f=5)[1]);ax[0].set_title('f = 5hz');ax[0].grid()
ax[1].step(Clock(f=10)[0],Clock(f=10)[1]);ax[1].set_title('f = 10hz');ax[1].grid()
ax[2].step(Clock(f=50)[0],Clock(f=50)[1]);ax[2].set_title('f = 50hz');ax[2].grid()
plt.show()