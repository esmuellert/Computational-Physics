# In[1]
import numpy as np
import matplotlib.pyplot as plt
import math

# In[2]
class canon_no_resistance(object):
    def __init__(self,v_0,theta,time_duration,time_step,g):
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
        # self.x_anly = np.arange(0,x_end,time_step)
        # self.y_anly = np.arange(0,x_end,time_step)
        self.v_y[0] = self.v_y_0
        self.time_step = time_step

    def calculate(self):
        for i in range(self.t.shape[0]-1):
            self.x[i+1] = self.x[i] + self.v_x * self.time_step
            self.v_y[i+1] = self.v_y[i] - self.g * self.time_step
            self.y[i+1] = self.y[i] + self.v_y[i] * self.time_step
            if self.y[i] < 0:
                print(i)
        #self.y_anly = self.x_anly*math.tan(self.theta) - self.g*np.square(self.x_anly)/(2*(self.v_0*math.cos(self.theta))**2)
    def plot(self):
        plt.plot(self.x,self.y,label = str(self.theta_0))
        #plt.plot(self.x_anly,self.y_anly)
    def plot_show(self):
        plt.title('no drag')
        plt.xlabel('x/km')
        plt.ylabel('y/km')
        plt.legend()
        plt.show()

canon_1 = canon_no_resistance(v_0=700,theta=30,time_duration=71.44,time_step=0.01,g=9.8)
canon_1.calculate()
canon_1.plot()
print(canon_1.x[-1])
canon_1 = canon_no_resistance(v_0=700,theta=35,time_duration=81.85,time_step=0.01,g=9.8)
canon_1.calculate()
canon_1.plot()

canon_1 = canon_no_resistance(v_0=700,theta=40,time_duration=91.84,time_step=0.01,g=9.8)
canon_1.calculate()
canon_1.plot()

canon_1 = canon_no_resistance(v_0=700,theta=45,time_duration=101.03,time_step=0.01,g=9.8)
canon_1.calculate()
canon_1.plot()

canon_1 = canon_no_resistance(v_0=700,theta=50,time_duration=109.45,time_step=0.01,g=9.8)
canon_1.calculate()
canon_1.plot()

canon_1 = canon_no_resistance(v_0=700,theta=55,time_duration=117.04,time_step=0.01,g=9.8)
canon_1.calculate()
canon_1.plot()

canon_1 = canon_no_resistance(v_0=700,theta=60,time_duration=123.73,time_step=0.01,g=9.8)
canon_1.calculate()
canon_1.plot()

canon_1.plot_show()

# In[3]

