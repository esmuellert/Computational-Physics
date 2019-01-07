# In[1]

import numpy as np
import matplotlib.pyplot as plt
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

        hamilton = -first
        return hamilton

    def interation(self):
        hamilton = self.calculate_hamilton(self.S)
        self.mag = np.array([np.sum(self.S)/100])
        self.hamilton = np.array([hamilton/100])

        for n in range(self.iter):
            i = random.randint(0, 9)
            j = random.randint(0, 9)
            self.S[i][j] = -self.S[i][j]
            hamilton_1 = self.calculate_hamilton(self.S)
            E_flip = (hamilton_1-hamilton)/2

            if E_flip<=0:
                hamilton = hamilton_1
                m = np.sum(self.S)/100
                self.mag = np.append(self.mag,m)
                self.hamilton = np.append(self.hamilton,hamilton/100)
                continue
            if E_flip>0:
                r = random.random()
                B = np.exp(-E_flip/(self.T))
                if r<=B:
                    hamilton = hamilton_1
                    m = np.sum(self.S)/100
                    self.mag = np.append(self.mag,m)
                    self.hamilton = np.append(self.hamilton,hamilton/100)
                    continue
                if r>B:
                    self.S[i][j] = -self.S[i][j]
                    m = np.sum(self.S)/100
                    self.mag = np.append(self.mag,m)
                    self.hamilton = np.append(self.hamilton,hamilton/100)                    
                    continue



    def plot_t(self):
        plt.plot(range(self.iter+1),self.mag)
        plt.xlabel("iteration")
        plt.title("Mean Magetization-Time  "+"T="+str(self.T))
        plt.ylabel("Mean Magetization")
        plt.show()                        





            


# In[2]
for t in [1.2,2.1,2.269,4]:
    ising=ising_model(T=t,iteration=100000)
    ising.interation()
    ising.plot_t()
    plt.savefig("T="+str(t)+".jpg")




# In[3]
mean_mag = np.array([])
temperature=np.arange(0.1,5,0.1)
for t in temperature:
        ising=ising_model(T=t,iteration=100000)
        ising.interation()
        mean_mag = np.append(mean_mag,np.mean(abs(ising.mag[30000:])))

def plot():
    plt.scatter(temperature,mean_mag)
    plt.xlabel("temperature")
    plt.title("Mean Magetization-Temperature Phase Graph")
    plt.ylabel("Mean Magetization")
    plt.show()
    plt.savefig("Mean Magetization-Temperature Phase Graph.jpg")

plot()


# In[4]
mean_energy = np.array([])
temperature=np.arange(0.1,5,0.1)
for t in temperature:
        ising=ising_model(T=t,iteration=10000)
        ising.interation()
        mean_energy = np.append(mean_energy,np.mean(ising.hamilton))

def plot():
    plt.scatter(temperature,mean_energy)
    plt.xlabel("temperature")
    plt.title("Mean Energy-Temperature Phase Graph")
    plt.ylabel("Mean Energy")
    plt.savefig("Mean Energy-Temperature Phase Graph.jpg")
    plt.show()


plot()
