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

    def promjena_indukcije(self,t):  #Može se staviti bilo koje pravilo po kojem se mjenja idukcija
        z_komponenta = t/10
        self.indukcija = np.array([0,0,z_komponenta])

    def promjena_elektricnog(self,t):
        self.E = np.array([0,0,0])    #može se zadati pravilo promjene

    def Runge_Kutta(self,x):
        t = 0
        while t < 10:
            if x == 1:
                self.promjena_indukcije(t)
                self.promjena_elektricnog(t)

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

    def liste(self):
        x_list = []
        y_list = []
        z_list = []

        for i in range(len(self.polozaji)):
            polozaj = self.polozaji[i]
            x = polozaj[0]
            y = polozaj[1]
            z = polozaj[2]
            x_list.append(x)
            y_list.append(y)
            z_list.append(z)
        return x_list,y_list,z_list

    def plot_usporedba(self):
        self.povratak()
        self.naboj = -1
        self.Runge_Kutta(0)
        x_elektron_konst,y_elektron_konst,z_elektron_konst = self.liste()
        
        self.povratak()
        self.Runge_Kutta(1)

        x_elektron_prom , y_elektron_prom ,z_elektron_prom = self.liste()
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x_elektron_konst, y_elektron_konst,z_elektron_konst,s = 1, label="Konstantno polje", c = 'r', marker='o')
        ax.scatter(x_elektron_prom,y_elektron_prom,z_elektron_prom,s = 1, label="Promjenjivo polje" , c = 'b', marker='o')
        ax.set_xlabel('X-os')
        ax.set_ylabel('Y-os')
        ax.set_zlabel('Z-os')
        ax.set_title("Elektron u magnetskom polju",fontsize = 14)
        ax.legend()

        plt.show()

    def plot_elektron_pozitron(self):
        self.povratak()
        self.naboj = 1
        self.Runge_Kutta(1)
        x_pozitron , y_pozitron , z_pozitron = self.liste()

        self.povratak()
        self.naboj = -1
        self.Runge_Kutta(1)

        x_elektron , y_elektron ,z_elektron = self.liste()
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x_pozitron, y_pozitron, z_pozitron,s = 1, label="Pozitron", c = 'r', marker='o')
        ax.scatter(x_elektron, y_elektron, z_elektron,s = 1, label="Elektron", c = 'b', marker='o')
        ax.set_xlabel('X-os')
        ax.set_ylabel('Y-os')
        ax.set_zlabel('Z-os')
        ax.legend()
        ax.set_title("Elektron i pozitron u magnetskom polju",fontsize = 14)

        plt.show()
        