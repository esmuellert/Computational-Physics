# In[1]

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import *
import random

class ising_model(object):
    def __init__(self,T,iteration):
        self.S = np.ones((10,10))
        self.T = T
        self.iter = iteration

    def calculate_hamilton(self,S):
        s_u = np.insert(S,0,values=0,axis=0)
        s_u = np.delete(s_u,-1,axis=0)
        
        s_d = np.insert(S,10,values=0,axis=0)
        s_d = np.delete(s_d,0,axis=0)
        
        s_l = np.insert(S,0,values=0,axis=1)
        s_l = np.delete(s_l,-1,axis=1)

        s_r = np.insert(S,10,values=0,axis=1)
        s_r = np.delete(s_r,0,axis=1)        

        first = (np.sum(S*s_u)+np.sum(S*s_d)+np.sum(S*s_l)+np.sum(S*s_r))
        second = -np.sum(S)

        hamilton = first
        return hamilton

    def interation(self):
        hamilton = self.calculate_hamilton(self.S)
        self.mag = np.array([np.sum(self.S)/100])
        for n in range(self.iter):
            i = random.randint(0, 9)
            j = random.randint(0, 9)
            self.S[i][j] = -self.S[i][j]
            hamilton_1 = self.calculate_hamilton(self.S)
            E_flip = hamilton_1-hamilton

            if E_flip<=0:
                hamilton = hamilton_1
                m = np.sum(self.S)/100
                self.mag = np.append(self.mag,m)
                continue
            if E_flip>0:
                r = random.random()
                B = np.exp(-E_flip/(self.T))
                if r<=B:
                    hamilton = hamilton_1
                    m = np.sum(self.S)/100
                    self.mag = np.append(self.mag,m)
                    continue
                if r>B:
                    self.S[i][j] = -self.S[i][j]
                    m = np.sum(self.S)/100
                    self.mag = np.append(self.mag,m)                    
                    continue


    def plot(self):
        plt.plot(range(self.iter+1),self.mag)
        plt.show()                        





            


# In[2]
ising=ising_model(T=2,iteration=1000)
ising.interation()
ising.plot()
ising.mag
# In[3]
import random
ising.calculate_hamilton(3*np.ones((10,10)))