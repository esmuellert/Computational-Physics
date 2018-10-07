# In[1]
import numpy as np
import matplotlib.pyplot as plt
import math

# In[2]
class canon_no_resistance(object):
    def __init__(self,v_0,theta,time_duration,time_step,g,x_end):
        self.theta_0 = theta
        self.theta = theta*math.pi/180
        self.v_0 = v_0
        self.v_x = v_0 * math.cos(self.theta)
        self.v_y_0 = v_0 * math.sin(self.theta)
        self.g = g
        self.t = np.arange(0,time_duration + time_step,time_step)
        self.x = np.arange(0,time_duration + time_step,time_step)
        self.y = np.arange(0,time_duration + time_step,time_step)
        self.v_y = np.arange(0,time_duration + time_step,time_step)
        self.x_anly = np.arange(0,x_end,1)
        self.y_anly = np.arange(0,x_end,1)
        self.v_y[0] = self.v_y_0
        self.time_step = time_step

    def calculate(self):
        for i in range(self.t.shape[0]-1):
            self.x[i+1] = self.x[i] + self.v_x * self.time_step
            self.v_y[i+1] = self.v_y[i] - self.g * self.time_step
            self.y[i+1] = self.y[i] + self.v_y[i] * self.time_step
            if self.y[i] < 0:
                print(i)
        self.y_anly = self.x_anly*math.tan(self.theta) - self.g*np.square(self.x_anly)/(2*(self.v_0*math.cos(self.theta))**2)
    def plot(self):
        plt.plot(self.x,self.y,label = str(self.theta_0))
        plt.plot(self.x_anly,self.y_anly)
    def plot_show(self):
        plt.title('no drag')
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.legend()
        plt.show()

canon_1 = canon_no_resistance(v_0=700,theta=30,time_duration=71.44,time_step=0.01,g=9.8,x_end=43308.19839244836)
canon_1.calculate()
canon_1.plot()

canon_1 = canon_no_resistance(v_0=700,theta=35,time_duration=81.85,time_step=0.01,g=9.8,x_end=46933.31637753981)
canon_1.calculate()
canon_1.plot()

canon_1 = canon_no_resistance(v_0=700,theta=40,time_duration=91.84,time_step=0.01,g=9.8,x_end=49247.46515922514)
canon_1.calculate()
canon_1.plot()

canon_1 = canon_no_resistance(v_0=700,theta=45,time_duration=101.03,time_step=0.01,g=9.8,x_end=50007.2986723011)
canon_1.calculate()
canon_1.plot()

canon_1 = canon_no_resistance(v_0=700,theta=50,time_duration=109.45,time_step=0.01,g=9.8,x_end=49247.172716140776)
canon_1.calculate()
canon_1.plot()

canon_1 = canon_no_resistance(v_0=700,theta=55,time_duration=117.04,time_step=0.01,g=9.8,x_end=46991.97027736777)
canon_1.calculate()
canon_1.plot()

canon_1 = canon_no_resistance(v_0=700,theta=60,time_duration=123.73,time_step=0.01,g=9.8,x_end=43305.50000000001)
canon_1.calculate()
canon_1.plot()

canon_1.plot_show()

# In[3]

class canon_resistance(object):
    def __init__(self,v_0,theta,time_duration,time_step,g,B2_sub_m):
        self.theta_0 = theta
        self.theta = theta*math.pi/180
        self.B2_sub_m = B2_sub_m
        self.v_0 = v_0
        self.v_x_0 = v_0 * math.cos(self.theta)
        self.v_y_0 = v_0 * math.sin(self.theta)
        self.g = g
        self.t = np.arange(0,time_duration + time_step,time_step)
        self.x = np.arange(0,time_duration + time_step,time_step)
        self.y = np.arange(0,time_duration + time_step,time_step)
        self.v_y = np.arange(0,time_duration + time_step,time_step)
        self.v_x = np.arange(0,time_duration+time_step,time_step)
        self.v_y[0] = self.v_y_0
        self.v_x[0] = self.v_x_0
        self.time_step = time_step

    def calculate(self):
        for i in range(self.t.shape[0]-1):
            self.v_x[i+1] = self.v_x[i] - self.B2_sub_m*self.v_0*self.v_x[i]*self.time_step
            self.x[i+1] = self.x[i] + self.v_x[i] * self.time_step
            self.v_y[i+1] = self.v_y[i] - self.g * self.time_step - self.B2_sub_m*self.v_0*self.v_y[i]*self.time_step
            self.y[i+1] = self.y[i] + self.v_y[i] * self.time_step

    def plot(self):
        plt.plot(self.x,self.y,label = str(self.theta_0))
   
    def plot_show(self):
        plt.title('with air drag')
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.legend()
        plt.show()

canon_2 = canon_resistance(v_0=700, theta=45, time_duration=100,time_step=0.01,g=9.8,B2_sub_m=0.00004)
canon_2.calculate()
canon_2.plot()
canon_2.plot_show()