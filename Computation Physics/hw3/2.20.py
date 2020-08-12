# In[1]
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
# In[2]
class ball(object):
    def __init__(self,v_0,theta,time_duration = 100,time_step = 0.0005,g = 9.8,B2_sub_m = 0.0054):
        self.theta_0 = theta
        self.theta = theta*math.pi/180
        self.B2_sub_m = B2_sub_m
        self.v_0 = v_0
        self.v_x_0 = v_0 * math.cos(self.theta)
        self.v_z_0 = v_0 * math.sin(self.theta)
        self.g = g
        self.t = np.arange(0,time_duration + time_step,time_step)
        self.x = np.arange(0,time_duration + time_step,time_step)
        self.y = np.arange(0,time_duration + time_step,time_step)
        self.z = np.arange(0,time_duration + time_step,time_step)
        self.v_y = np.arange(0,time_duration + time_step,time_step)
        self.v_x = np.arange(0,time_duration+time_step,time_step)
        self.v_z = np.arange(0,time_duration+time_step,time_step)
        self.v_z[0] = self.v_z_0
        self.v_x[0] = self.v_x_0
        self.time_step = time_step
        self.i = 0
    def calculate_with_drag(self):
        for i in range(self.t.shape[0]-1):
            self.v_x[i+1] = self.v_x[i] - self.B2_sub_m*math.sqrt(self.v_x[i]**2+self.v_y[i]**2+self.v_z[i]**2)*self.v_x[i]*self.time_step
            self.x[i+1] = self.x[i] + self.v_x[i] * self.time_step
            self.v_y[i+1] = self.v_y[i] - self.g * self.time_step - self.B2_sub_m*math.sqrt(self.v_x[i]**2+self.v_y[i]**2+self.v_z[i]**2)*self.v_y[i]*self.time_step
            self.y[i+1] = self.y[i] + self.v_y[i] * self.time_step
            self.v_z[i+1] = self.v_z[i] + 0.423*self.g*self.time_step-self.B2_sub_m*math.sqrt(self.v_x[i]**2+self.v_y[i]**2+self.v_z[i]**2)*self.v_z[i]*self.time_step
            self.z[i+1] = self.z[i] + self.v_z[i]*self.time_step

    def plot(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(self.x,self.z,self.y)

    def plot_show(self):
        plt.title('with air drag')
        plt.xlabel('x/m')
        plt.ylabel('z/m')
        plt.show()

baseball = ball(v_0=40,theta=20,time_duration=1)
baseball.calculate_with_drag()
baseball.plot()
baseball.plot_show()