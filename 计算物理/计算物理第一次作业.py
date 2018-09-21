import numpy as np
import math

import matplotlib.pyplot as pl
class uranium_decay:
    """
    Simulation of radioactive decay
    Program to accompany 'Computational Physics' by Cai Hao
    """
    def __init__(self, number_of_nuclei = 100, time_constant = 1, time_of_duration = 10, time_step = 0.05,t = np.linspace(0,10,100),anality_N = np.linspace(0,10,100)):
        # unit of time is second
        self.n_uranium = [number_of_nuclei]
        self.number_of_nuclei = number_of_nuclei
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.t_0 = t
        self.anality_N = anality_N
        print("Initial number of nuclei ->", number_of_nuclei)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmp = self.n_uranium[i] - self.n_uranium[i] / self.tau * self.dt
            self.n_uranium.append(tmp)
            self.t.append(self.t[i] + self.dt)
        self.anality_N = self.number_of_nuclei*math.e**(-self.t_0/self.tau)
    def show_results(self):
        pl.plot(self.t, self.n_uranium,color = 'blue')
        pl.plot(self.t_0,self.anality_N,color = 'red')
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.show()
    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n_uranium[i], file = myfile)
        myfile.close()


N_A = uranium_decay()
N_A.calculate()
N_A.show_results()
N_A.store_results()

N_Anum = np.genfromtxt("nuclei_decay_data.txt")

class solve_N_B(uranium_decay):
    def __init__(self, number_of_nuclei = 100, time_constant = 1, time_of_duration = 10, time_step = 0.05,t = np.linspace(0,10,201),anality_N = np.linspace(0,10,201)):
        # unit of time is second
        self.n_uranium = [number_of_nuclei]
        self.t = [0]
        self.number_of_nuclei = number_of_nuclei
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.t_0 = t
        print("Initial number of nuclei ->", number_of_nuclei)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
        
    def calculate(self,N_A,N_A_tau):
        for i in range(self.nsteps):
            tmp = self.n_uranium[i] + (N_A[i,1]/N_A_tau-self.n_uranium[i]/self.tau)*self.dt
            self.n_uranium.append(tmp)
            self.t.append(self.t[i] + self.dt)
        for i in range(self.nsteps):
            self.anality_N = 100*(self.tau/(N_A_tau-self.tau))*math.e**(-self.t_0/N_A_tau)
    def show_results(self):
        pl.plot(self.t, self.n_uranium,color = 'blue')
        pl.plot(self.t_0,self.anality_N,color = 'red')
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.show()
        
N_B = solve_N_B()
N_B.calculate(N_Anum,2)
N_B.show_results()
