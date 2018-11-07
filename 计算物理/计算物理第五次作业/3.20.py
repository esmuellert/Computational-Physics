# In[1]
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math
import time

class pendulum(object):
    def __init__(self,angle_0, omega_0, F_D,time_step=0.04, g=9.8,l=9.8,q=0.5,m=0.1,omega_D=2/3):
        self.g = g
        self.q = q
        self.l = l
        self.m = m
        self.omega_D = omega_D
        self.angle_0 = angle_0
        self.angle_1 = self.angle_0
        self.omega_0 = omega_0
        self.omega_1 = self.omega_0 * math.pi / 180
        self.F_D=F_D
        self.E_0=0
        self.time_total=400*(2*math.pi/omega_D)
        self.time_step=time_step
        self.t = np.arange(0, self.time_total + time_step, time_step)
        self.angle = np.arange(0, self.time_total + time_step, time_step)
        self.angle1 = np.arange(0, self.time_total + time_step, time_step)
        self.omega = np.arange(0, self.time_total + time_step, time_step)
        self.t[0] = 0
        self.angle[0] = self.angle_1
        self.angle1[0] = self.angle_1
        self.omega[0] = self.omega_1
        self.time_step = time_step
        self.i = 0


    def calculate(self):
        for i in range(self.t.shape[0] - 1):
           self.omega[i+1] = self.omega[i]-((self.g/self.l)*math.sin(self.angle1[i])+self.q*self.omega[i]-self.F_D*math.sin(self.omega_D*self.t[i]))*self.time_step
           self.angle[i+1] = self.angle1[i]+self.omega[i+1]*self.time_step
           if self.angle[i+1] > math.pi:
            self.angle1[i+1] = self.angle[i+1] - 2*math.pi
           elif self.angle[i+1] < -math.pi:
             self.angle1[i+1] = self.angle[i+1] + 2*math.pi
           else:
            self.angle1[i+1] = self.angle[i+1]
           

def calculate_plot(step):
    F_D = np.arange(1.35,1.5,step)
    theta = np.array([])
    for j in [1.69,2.82,2.72,1.52]:
        for i in F_D:
            pendulum1 = pendulum(j,0,i)
            pendulum1.calculate()
            if pendulum1.angle1[-1]<0:
                pendulum1.angle1[-1] = 4+pendulum1.angle1[-1]
            theta = np.append(theta,pendulum1.angle1[-1])
        plt.scatter(F_D,theta,s=8,color='blue')

        theta = np.array([])
    
    
    plt.xlabel("F_D")
    plt.ylabel("theta")
    # plt.show()
# In[2]

start = time.time()
calculate_plot(0.01)
end = time.time()
print(end-start)