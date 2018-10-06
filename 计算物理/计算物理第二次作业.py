# In[1]
import numpy as np
import matplotlib.pyplot as plt
import math

# In[2]
class canon(object):
    def __init__(self,v_0,theta,time_duration,time_step,g):
        self.v_x = v_0 * math.cos(theta)
        self.v_y_0 = v_0 * math.sin(theta)
        self.g = g
        self.t = np.arange(0,time_duration + time_step,time_step)
        self.x = np.arange(0,time_duration + time_step,time_step)
        self.y = np.arange(0,time_duration + time_step,time_step)
        self.v_y = np.arange(0,time_duration + time_step,time_step)
        self.y[0] = self.v_y_0
        self.time_step = time_step

    def calculate(self):
        for i in range(self.t.shape[0]-1):
            self.x[i+1] = self.x[i] + self.v_x * self.time_step
            self.v_y[i+1] = self.v_y[i] - self.g * self.time_step
            self.y[i+1] = self.y[i] + self.v_y[i] * self.time_step
    
    def plot(self):
        plt.plot(self.x,self.y)
        plt.show()

canon_1 = canon(v_0=100,theta=math.pi/4,time_duration=10,time_step=0.01,g=9.8)
canon_1.calculate()
canon_1.plot()