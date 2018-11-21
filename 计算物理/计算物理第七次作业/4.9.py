# In[1]
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math
import time
from multiprocessing import Pool

np.set_printoptions(threshold=np.inf)

class trace(object):
    def __init__(self,x_0,y_0,v_0,beta,time_step=0.01,time_total=100):
        self.v_x0 = 0
        self.v_y0 = v_0
        self.x_0 = x_0
        self.y_0 = y_0
        self.time_total=time_total
        self.time_step=time_step
        self.t = np.arange(0, self.time_total + time_step, time_step)
        self.x = np.arange(0, self.time_total + time_step, time_step)
        self.y = np.arange(0, self.time_total + time_step, time_step)        
        self.v_x = np.arange(0, self.time_total + time_step, time_step)
        self.v_y = np.arange(0, self.time_total + time_step, time_step)
        self.v = np.arange(0, self.time_total + time_step, time_step)
        self.r = np.arange(0, self.time_total + time_step, time_step)
        self.t[0] = 0
        self.x[0] = self.x_0
        self.y[0] = self.y_0
        self.v_x[0] = self.v_x0
        self.v_y[0] = self.v_y0
        self.beta = beta
        self.r[0] = 1

    def calculate(self):
        for i in range(self.t.shape[0] - 1):

            self.v_x[i+1] = -4*math.pi**2*self.x[i]/(self.r[i]**(self.beta+1))*self.time_step + self.v_x[i]
            self.v_y[i+1] = -4*math.pi**2*self.y[i]/(self.r[i]**(self.beta+1))*self.time_step + self.v_y[i]
            self.x[i+1] = self.x[i] + self.v_x[i+1]*self.time_step
            self.y[i+1] = self.y[i] + self.v_y[i+1]*self.time_step            
            self.r[i+1] = math.sqrt(self.x[i+1]**2+self.y[i+1]**2)
    def plot(self):
        fig=plt.figure(figsize=[8,8]) 
        plt.plot(self.x,self.y)
        plt.scatter([0],[0],s=1000,color='yellow')
        plt.xlabel('x(AU)')
        plt.ylabel('y(AU)')
        plt.title("beta="+str(self.beta)+",e="+str(self.x[0]-1))
        plt.show()

start = time.time()
a = trace(x_0=1.5,y_0=0,v_0=2*math.pi,beta=2.05)
a.calculate()
a.plot()
end = time.time()
end-start
