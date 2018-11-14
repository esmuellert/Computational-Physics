# In[1]
import numpy as np
import matplotlib.pyplot as plt
from math import *

class pendulum():
    def __init__(self, initial_angle = 0.2, initial_omega = 0, amplitude = 1.44, frequency = 2 / 3, damping = 0.5, total_time = 100):
        self.w = [initial_omega]
        self.theta = [initial_angle]
        self.f = amplitude
        # 给出单摆的其他参数
        self.l = 9.8
        self.dt = 0.001 # 方便取驱动力周期的整数倍
        self.t = np.arange(0., total_time, self.dt)
        self.q = damping  # 阻尼系数
        self.omega_D = frequency  # 驱动力角频率
        self.g = 9.8  # 重力加速度

    def run(self, min_theta = 0):
        self.theta_need = []
        for t in np.delete(self.t, -1):
            tmp_w = self.w[-1] - ((self.g / self.l) * sin(self.theta[-1]) + self.q * self.w[-1] - self.f * sin(self.omega_D * t))* self.dt
            self.w.append(tmp_w)
            tmp_theta = self.theta[-1] + self.w[-1] * self.dt
            if tmp_theta > pi:
                tmp_theta -= 2 * pi
            elif tmp_theta < -pi:
                tmp_theta += 2 * pi
            self.theta.append(tmp_theta)

    def show(self, k): 
        # FFT变换部分
        self.theta = np.array(self.theta)
        #self.theta -= sum(self.theta) / len(self.theta) # 根据陈耿剑同学的方法，去掉加入的方波的影响
        self.fft = np.fft.fft(self.theta)
        n = len(self.theta) / 500 # 只截取前面一小部分，足以看出频谱的变化
        frequency = np.arange(n / 2) # 这里的频率没有调整成课本上的范围，水平有限
        nfft = abs(self.fft[range(int(n / 2))] / n)  

        plt.subplot(k)
        plt.plot(frequency / 50, nfft, linewidth = 1) # 参考课本上，把频率搞成了0-2
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Power')
        plt.text(1.5, 150, r'$F_D=%s$'% self.f, size = 13)
        return n
if __name__ == '__main__':
    plt.figure(figsize = (10,6), dpi=80)
    a = pendulum()
    a.run()
    n = a.show(111)
    print(n)
