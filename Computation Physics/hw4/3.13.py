# In[1]
import numpy as np
import matplotlib.pyplot as plt
import math

class pendulum(object):
    def __init__(self, F_D,theta_0=0.2,alpha_0=0.3, time_total=60,omega_0=0, time_step=0.04, g=9.8,l=9.8,q=0.5,m=0.1,omega_D=2/3,Omega_0=0,Omega_D=2/3):
        self.g = g
        self.q = q
        self.l = l
        self.m = m
        self.F_D=F_D
        self.theta_0 = theta_0
        self.omega_0 = omega_0
        self.omega_D = omega_D
        self.Omega_0 = Omega_0
        self.Omega_D = Omega_D
        self.alpha_0 = alpha_0
        self.delta_0=0.001
        self.time_total=time_total
        self.time_step=time_step
        self.t = np.arange(0, time_total + time_step, time_step)
        self.theta = np.arange(0, time_total + time_step, time_step)
        self.theta1 = np.arange(0, time_total + time_step, time_step)
        self.omega = np.arange(0, time_total + time_step, time_step)
        self.Omega = np.arange(0, time_total + time_step, time_step)
        self.alpha = np.arange(0, time_total + time_step, time_step)
        self.alpha1 = np.arange(0, time_total + time_step, time_step)
        self.delta= np.arange(0, time_total + time_step, time_step)
        self.t[0] = 0
        self.theta[0] = self.theta_0
        self.theta1[0] = self.theta_0
        self.omega[0] = self.omega_0
        self.Omega[0] = self.Omega_0
        self.alpha[0] = self.alpha_0
        self.alpha1[0] = self.alpha_0
        self.delta[0]=self.delta_0
        self.i = 0

    def calculate(self):
        for i in range(self.t.shape[0] - 1):
            self.omega[i+1] = self.omega[i]-((self.g/self.l)*math.sin(self.theta1[i])+self.q*self.omega[i]-self.F_D*math.sin(self.omega_D*self.t[i]))*self.time_step
            self.theta[i+1] = self.theta1[i]+self.omega[i+1]*self.time_step
            if self.theta[i+1] > math.pi:
                self.theta1[i+1] = self.theta[i+1] - 2*math.pi
            elif self.theta[i+1] < -math.pi:
                self.theta1[i+1] = self.theta[i+1] + 2*math.pi
            else:
                self.theta1[i+1] = self.theta[i+1]

            self.Omega[i+1] = self.Omega[i]-((self.g/self.l)*math.sin(self.alpha1[i])+self.q*self.Omega[i]-self.F_D*math.sin(self.Omega_D*self.t[i]))*self.time_step
            self.alpha[i+1] = self.alpha1[i]+self.Omega[i+1]*self.time_step
            if self.alpha[i+1] > math.pi:
                self.alpha1[i+1] = self.alpha[i+1] - 2*math.pi
            elif self.alpha[i+1] < -math.pi:
                self.alpha1[i+1] = self.alpha[i+1] + 2*math.pi
            else:
                self.alpha1[i+1] = self.alpha[i+1]
            if abs(self.alpha1[i+1]-self.theta1[i+1])>math.pi:
                self.delta[i+1]=2*math.pi-abs(self.alpha1[i+1]-self.theta1[i+1])
            else:
                self.delta[i+1]=abs(self.alpha1[i+1]-self.theta1[i+1])
        self.delta = np.log(np.abs(self.delta))
        self.alpha = np.log(np.abs(self.alpha))
        self.theta = np.log(np.abs(self.theta))
        

    def plot(self):
        plt.plot(self.t,self.delta,label='delta')
        

    def plot_show(self,name):
        plt.title(name)
        plt.xlabel('t/s')
        plt.ylabel('E/J')
        plt.legend()
        plt.show()


pendulum1 = pendulum(3)
pendulum1.calculate()
pendulum1.plot()
pendulum1.plot_show(name="The E-t cruve,F_D=1.2,delta")