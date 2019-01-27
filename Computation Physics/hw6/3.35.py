# In[1]
import numpy as np
import matplotlib.pyplot as plt
import math

class pendulum(object):
    def __init__(self,theta_0=0.2, omega_0=0, F_D=0.5, time_duration=60, time_step=0.01, g=9.8,l=9.8,q=0.5,m=0.1,omega_D=2/3):
        self.g = g
        self.q = q
        self.l = l
        self.m = m
        self.omega_D = omega_D
        self.theta_0 = theta_0
        self.omega_0 = omega_0
        self.F_D=F_D
        self.time_duration=time_duration
        self.time_step=time_step
        self.t = np.arange(0, time_duration + time_step, time_step)
        self.theta = np.arange(0, time_duration + time_step, time_step)
        self.omega = np.arange(0, time_duration + time_step, time_step)
        self.theta[0] = self.theta_0
        self.omega[0] = self.omega_0

    def calculate(self):
        for i in range(self.t.shape[0] - 1):
           self.omega[i+1] = self.omega[i]-((self.g/self.l)*math.sin(self.theta[i])+self.q*self.omega[i]-self.F_D*math.sin(self.omega_D*self.t[i]))*self.time_step
           self.theta[i+1] = self.theta[i]+self.omega[i+1]*self.time_step
           if self.theta[i+1] > math.pi:
            self.theta[i+1] = self.theta[i+1] - 2*math.pi
           if self.theta[i+1] < -math.pi:
             self.theta[i+1] = self.theta[i+1] + 2*math.pi
        self.theta = abs(np.fft.fft(self.theta))
    def plot(self):
        plt.plot(self.t[1:100], self.theta[1:100]/1000, linewidth = 1)
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power')
        plt.show()

a = pendulum()
a.calculate()
a.plot()