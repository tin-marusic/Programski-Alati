import numpy as np
import matplotlib.pyplot as plt

class Electromagnetic:
    def __init__(self,m,y0,x0,z0,q,v,B,E):
        self.masa = m
        self.polozaj = np.array([x0,y0,z0])
        self.polozaj0 = np.array([x0,y0,z0])
        self.polozaji = [self.polozaj]
        self.naboj = q
        self.indukcija = B
        self.v0 = v
        self.brzina = v
        self.E = E
        self.dt = 0.01

    def reset(self):
        del self.polozaji
        del self.masa
        del self.polozaj0
        del self.polozaj
        del self.naboj
        del self.indukcija
        del self.v0
        del self.brzina
        del self.E
        del self.dt

    def povratak(self):
        del self.polozaj
        del self.brzina
        self.polozaji.clear()
        self.polozaj = self.polozaj0
        self.brzina = self.v0

    def akceleracija(self,brzina):
        akc = (np.dot(self.naboj,self.E )+np.dot(self.naboj,np.cross(brzina,self.indukcija)))/self.masa
        return akc

    def Runge_Kutta(self):
        t = 0
        while t < 20:
            k1v = self.akceleracija(self.brzina) * self.dt
            k1 = np.dot(self.brzina,self.dt)

            k2v = self.akceleracija(self.brzina + 0.5 * k1v) * self.dt
            k2 = (self.brzina + 0.5 * k1v)*self.dt

            k3v = self.akceleracija(self.brzina + 0.5 * k2v) * self.dt
            k3 = (self.brzina + 0.5 * k2v)*self.dt

            k4v = self.akceleracija(self.brzina + 0.5 * k3v) * self.dt
            k4 = (self.brzina + 0.5 * k3v)*self.dt

            self.brzina = self.brzina + (1/6)*(k1v + 2 * k2v + 2 * k3v + k4v)
            self.polozaj = self.polozaj + (1/6)*(k1 + 2 * k2 + 2 * k3 + k4)
            self.polozaji.append(self.polozaj)
            t = t + self.dt
       
    def Euler(self):
        t = 0
        while t<20:
            a = self.akceleracija(self.brzina)
            self.brzina = a * self.dt + self.brzina
            self.polozaj = self.polozaj + self.brzina*self.dt
            self.polozaji.append(self.polozaj)
            t = t + self.dt

    def plot(self):
        self.naboj = 1
        self.Runge_Kutta()
        x_pozitron = []
        y_pozitron = []
        z_pozitron = []
        x_elektron = []
        y_elektron = []
        z_elektron = []

        for i in range(len(self.polozaji)):
            polozaj = self.polozaji[i]
            x = polozaj[0]
            y = polozaj[1]
            z = polozaj[2]
            x_pozitron.append(x)
            y_pozitron.append(y)
            z_pozitron.append(z)
        
        self.povratak()
        self.naboj = -1
        self.Runge_Kutta()

        for i in range(len(self.polozaji)):
            polozaj = self.polozaji[i]
            x = polozaj[0]
            y = polozaj[1]
            z = polozaj[2]
            x_elektron.append(x)
            y_elektron.append(y)
            z_elektron.append(z)
         
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x_pozitron, y_pozitron, z_pozitron,s = 1, label="Pozitron", c = 'r', marker='o')
        ax.scatter(x_elektron, y_elektron, z_elektron,s = 1, label="Elektron", c = 'b', marker='o')
        ax.set_xlabel('X-os')
        ax.set_ylabel('Y-os')
        ax.set_zlabel('Z-os')
        ax.legend()

        plt.show()
    
    def plot_euler_runge(self):
        self.Runge_Kutta()
        x_runge = []
        y_runge = []
        z_runge = []
        x_euler = []
        y_euler = []
        z_euler = []

        for i in range(len(self.polozaji)):
            polozaj = self.polozaji[i]
            x = polozaj[0]
            y = polozaj[1]
            z = polozaj[2]
            x_runge.append(x)
            y_runge.append(y)
            z_runge.append(z)

        self.povratak()

        self.Euler()
        for i in range(len(self.polozaji)):
            polozaj = self.polozaji[i]
            x = polozaj[0]
            y = polozaj[1]
            z = polozaj[2]
            x_euler.append(x)
            y_euler.append(y)
            z_euler.append(z)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x_runge, y_runge, z_runge,s = 1, label="Runge_Kutta", c = 'r', marker='o')
        ax.scatter(x_euler, y_euler, z_euler,s = 1, label="Euler", c = 'b', marker='o')
        ax.set_xlabel('X-os')
        ax.set_ylabel('Y-os')
        ax.set_zlabel('Z-os')
        ax.legend()

        plt.show()