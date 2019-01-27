# In[1]
import numpy as np
import matplotlib.pyplot as plt
import math

class pendulum(object):
    def __init__(self,theta_0, omega_0, F_D, time_duration=60, time_step=0.04, g=9.8,l=9.8,q=0.5,m=0.1,omega_D=2/3):
        self.g = g
        self.q = q
        self.l = l
        self.m = m
        self.omega_D = omega_D
        self.theta_0 = theta_0
        self.theta_1 = self.theta_0
        self.omega_0 = omega_0
        self.omega_1 = self.omega_0 * math.pi / 180
        self.F_D=F_D
        self.E_0=self.m*self.g*self.l*(1-math.cos(self.theta_0))
        self.time_duration=time_duration
        self.time_step=time_step
        self.t = np.arange(0, time_duration + time_step, time_step)
        self.theta = np.arange(0, time_duration + time_step, time_step)
        self.theta1 = np.arange(0, time_duration + time_step, time_step)
        self.omega = np.arange(0, time_duration + time_step, time_step)
        self.E = np.arange(0, time_duration + time_step, time_step)
        self.t[0] = 0
        self.theta[0] = self.theta_1
        self.theta1[0] = self.theta_1
        self.omega[0] = self.omega_1
        self.E[0] = self.E_0
        self.time_step = time_step
        self.i = 0



    def calculate(self):
        for i in range(self.t.shape[0] - 1):
           self.omega[i+1] = self.omega[i]-((self.g/self.l)*math.sin(self.theta[i])+self.q*self.omega[i]-self.F_D*math.sin(self.omega_D*self.t[i]))*self.time_step
           self.theta[i+1] = self.theta[i]+self.omega[i+1]*self.time_step
           if self.theta[i+1] > math.pi:
            self.theta1[i+1] = self.theta[i+1] - 2*math.pi
           elif self.theta[i+1] < math.pi:
             self.theta1[i+1] = self.theta[i+1] + 2*math.pi
           else:
            self.theta1[i+1] = self.theta[i+1]

           self.E[i+1]=0.5*self.m*(self.l**2)*(self.omega[i+1]**2)+self.m*self.g*(1-math.cos(self.theta1[i+1]))


    def plot_2D(self):
        plt.plot(self.t, self.E, label=self.F_D)

    def plot_show_2D(self):
        plt.title('The relation of E-T')
        plt.xlabel('t/s')
        plt.ylabel('E/J')
        plt.legend()
        plt.show()


pendulum1 = pendulum(0.2,0,0)
pendulum1.calculate()
pendulum1.plot_2D()

pendulum1 = pendulum(0.2,0,0.5)
pendulum1.calculate()
pendulum1.plot_2D()

pendulum1 = pendulum(0.2,0,1.2)
pendulum1.calculate()
pendulum1.plot_2D()

pendulum1.plot_show_2D()