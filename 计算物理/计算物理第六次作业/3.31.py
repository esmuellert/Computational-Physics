# In[1]
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math
import time
from multiprocessing import Pool

np.set_printoptions(threshold=np.inf)

class billiard(object):
    def __init__(self,theta_0,x_0,y_0,v_0,time_step=0.01,time_total=200):
        self.theta_0 = theta_0
        self.omega_0 = math.atan2(y_0,x_0)
        self.v_x0 = v_0*math.cos(theta_0)
        self.v_y0 = v_0*math.sin(theta_0)
        self.x_0 = x_0
        self.y_0 = y_0
        self.time_total=time_total
        self.time_step=time_step
        self.t = np.arange(0, self.time_total + time_step, time_step)
        self.omega = np.arange(0, self.time_total + time_step, time_step)
        self.theta = np.arange(0, self.time_total + time_step, time_step)
        self.x = np.arange(0, self.time_total + time_step, time_step)
        self.y = np.arange(0, self.time_total + time_step, time_step)        
        self.v_x = np.arange(0, self.time_total + time_step, time_step)
        self.v_y = np.arange(0, self.time_total + time_step, time_step)
        self.v = np.arange(0, self.time_total + time_step, time_step)
        self.t[0] = 0
        self.theta[0] = self.theta_0
        self.omega[0] = self.omega_0
        self.x[0] = self.x_0
        self.y[0] = self.y_0
        self.v_x[0] = self.v_x0
        self.v_y[0] = self.v_y0
        self.ye0 = np.array([],dtype=int)
        self.x0 = np.array([])
        self.vx_e0  = np.array([])

    def calculate(self):
        for i in range(self.t.shape[0] - 1):
            self.x[i+1] = self.x[i] + self.v_x[i]*self.time_step
            self.y[i+1] = self.y[i] + self.v_y[i]*self.time_step
            self.v_x[i+1] = self.v_x[i]
            self.v_y[i+1] = self.v_y[i]
            self.theta = np.arctan2(self.v_y,self.v_x)
            self.omega = np.arctan2(self.y,self.x)
            self.v = np.sqrt(self.v_x**2+self.v_y**2)

            if self.x[i+1]>=2 or self.x[i+1]<=-2:
                self.v_x[i+1] = -self.v_x[i+1]
            if self.y[i+1]>=2 or self.y[i+1]<=-2:
                self.v_y[i+1] = -self.v_y[i+1]

            if self.x[i+1]**2+self.y[i+1]**2<=1:
                self.v_x[i+1] = -math.cos(2*self.omega[i+1]-self.theta[i+1])*self.v[i+1]
                self.v_y[i+1] = -math.sin(2*self.omega[i+1]-self.theta[i+1])*self.v[i+1]

            if (self.y[i]<=0 and self.y[i+1]>=0) or (self.y[i]>=0 and self.y[i+1]<=0):
                if abs(self.y[i])-abs(self.y[i+1])>=0:
                    self.ye0 = np.append(self.ye0,i+1)
                if abs(self.y[i])-abs(self.y[i+1])<0:
                    self.ye0 = np.append(self.ye0,i)

    def plot_x_y(self):
        plt.plot([-2,0,2],[-2,-2,-2],color='black')
        plt.plot([-2,0,2],[2,2,2],color='black')
        plt.plot([-2,-2,-2],[-2,0,2],color='black')
        plt.plot([2,2,2],[-2,0,2],color='black')
        plt.plot(self.x,self.y,linewidth=1)

        theta = np.linspace(0, 2*np.pi,800)
        x,y = np.cos(theta), np.sin(theta)
        plt.plot(x, y,linewidth=2.0)
        plt.axis('square')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Graph of trace")
        plt.show()
    
    def plot_phase(self):
        self.x0 = self.x[self.ye0]
        self.v_xe0  = self.v_x[self.ye0]
        plt.scatter(self.x0,self.v_xe0,s=2)
        plt.xlabel("x")
        plt.ylabel("v_x")
        plt.title("Phase-space plot")
        plt.show()       
start = time.time()
billiard1 = billiard(theta_0=1,x_0=1.54,y_0=0.86,v_0=8)
billiard1.calculate()
billiard1.plot_x_y()
billiard1.plot_phase()
end = time.time()
print(end-start)
# In[2]

