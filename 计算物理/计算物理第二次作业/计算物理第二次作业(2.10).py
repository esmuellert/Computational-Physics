# In[1]
import numpy as np
import matplotlib.pyplot as plt
import math


# In[2]

class canon_resistance(object):
    def __init__(self,v_0,theta,time_duration = 100,time_step = 0.1,g = 9.8,B2_sub_m = 0.00004,distance = 11088):
        self.theta_0 = theta
        self.theta = theta*math.pi/180
        self.B2_sub_m = B2_sub_m
        self.distance = distance
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
        self.i = 0
        self.pos = [1,2]
    def calculate_with_drag(self):
        for i in range(self.t.shape[0]-1):
            self.v_x[i+1] = self.v_x[i] - self.B2_sub_m*self.v_0*self.v_x[i]*self.time_step
            self.x[i+1] = self.x[i] + self.v_x[i] * self.time_step
            self.v_y[i+1] = self.v_y[i] - self.g * self.time_step - self.B2_sub_m*self.v_0*self.v_y[i]*self.time_step
            self.y[i+1] = self.y[i] + self.v_y[i] * self.time_step
            if self.x[i]>=self.distance:
                self.i = i
                break
                

    def get_position(self):
        self.pos[0] = self.y[self.i-1]
        self.pos[1] = self.y[self.i]
        return self.pos

    def plot(self):
        plt.plot(self.x,self.y,label = str(self.theta_0))
   
    def plot_show(self):
        plt.title('with air drag')
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.legend()
        plt.show()

def find_v_min(altitude):
    v_0 ,v_min,theta = 650,900,45
    for i in range(1000):
        v_0 = v_0 + 0.1
        canon = canon_resistance(v_0=v_0, theta=theta)
        canon.calculate_with_drag()
        pos = canon.get_position()
        if (altitude >= pos[0] and altitude<= pos[1]) or (altitude >= pos[1] and altitude <= pos[0]):
            if v_0<v_min:
                v_min = v_0    
    return v_min
a = find_v_min(altitude=7000)
print(a)
