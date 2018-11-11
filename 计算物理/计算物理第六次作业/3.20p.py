# In[1]
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math
import time
from multiprocessing import Pool

class pendulum(object):
    def __init__(self,theta_0,x_0,y_0,v_0,time_step=0.01,time_total=100):
        self.theta_0 = theta_0
        self.omega_0 = math.atan2(y_0,x_0)
        self.v_x0 = v_0*math.cos(theta_0)
        self.v_y0 = v_0*math.sin(theta_0)
        self.x_0 = x_0
        self.y_0 = y_0
        self.time_total=time_total
        self.time_step=time_step
        self.oemga = np.arange(0, self.time_total + time_step, time_step)
        self.theta = np.arange(0, self.time_total + time_step, time_step)
        self.x = np.arange(0, self.time_total + time_step, time_step)
        self.y = np.arange(0, self.time_total + time_step, time_step)        
        self.v_x = np.arange(0, self.time_total + time_step, time_step)
        self.v_y = np.arange(0, self.time_total + time_step, time_step)
        self.t[0] = 0
        self.theta[0] = self.theta_0
        self.omega[0] = self.omega_0
        self.x[0] = self.x_0
        self.y[0] = self.y_0
        self.v_x[0] = self.v_x0
        self.v_y[0] = self.v_y0


    def calculate(self):
        for i in range(self.t.shape[0] - 1):
            self.x[i+1] = self.x[i] + self.v_x[i]*self.time_step
            self.y[i+1] = self.y[i] + self.v_y[i]*self.time_step
            self.v_x[i+1] = self.v_x[i]
            self.v_y[i+1] = self.v_y[i]
            self.theta = np.arctan2(self.v_y,self.v_x)
            self.omega = np.arctan2(self.y,self.x)

            if self.x[i+1]>=2 or self.x[i+1]<=-2:
                self.v_x[i+1] = -self.v_x[i+1]
            if self.y[i+1]>=2 or self.y[i+1]<=-2:
                self.v_y[i+1] = -self.v_y[i+1]

            
           







# In[2]
if __name__ == '__main__':

    start = time.time()
    calculate_plot(0.0001)
    end = time.time()
    print(end-start)




