import numpy as np
import math as m
import matplotlib.pyplot as plt

class sun_earth:
    def __init__(self,m1,m2,v1,v2,cord1,cord2,vrijeme):
        self.masa1 = m1
        self.masa2 = m2
        self.brzina1 = v1
        self.brzina0 = v1
        self.brzina02 = v2
        self.brzina2 = v2
        self.polozaj1 = cord1
        self.polozaj0 = cord1
        self.polozaj02 = cord2
        self.polozaj2 = cord2
        self.dt = 36000
        self.dan = 0
        self.G = 6.67 * (10 **-11 )
        self.polozaji1 = []
        self.polozaji2 = []
        self.vrijeme = vrijeme

    def restart(self):
        self.polozaj1 = self.polozaj0
        self.polozaj2 = self.polozaj02
        self.brzina1 = self.brzina0
        self.brzina2 = self.brzina02
        self.dan = 0 
        self.polozaji1.clear()
        self.polozaji2.clear()

    def reset(self):
        del self.vrijeme
        del self.masa1
        del self.masa2
        del self.brzina1
        del self.brzina2
        del self.brzina0
        del self.brzina02
        del self.polozaj1
        del self.polozaj2
        del self.polozaj0
        del self.polozaj02
        del self.dt
        del self.dan
        del self.polozaji1
        del self.polozaji2

    def akc(self,x,y):
        udaljenost = np.linalg.norm(abs(np.subtract(self.polozaj1+x,self.polozaj2+y)))**3
        akc1 = -self.G * (self.masa2 * (np.subtract(self.polozaj1+x,self.polozaj2+y))/ udaljenost)
        for i in range(3):
            if m.isnan(akc1[i])==True:
                akc1[i ]= 0
        akc2 = -self.G * (self.masa1 * (np.subtract(self.polozaj2+y,self.polozaj1+x))/udaljenost)
        for i in range(3):
            if m.isnan(akc2[i])==True:
                akc2[i ]= 0
        return akc1,akc2

    def Euler(self):
        while self.dan < self.vrijeme:
            a,b = self.akc(0,0)
            self.brzina1 = np.add(self.brzina1,a*self.dt)
            self.polozaj1 = np.add(self.polozaj1 , self.brzina1 * self.dt)
            self.polozaji1.append(self.polozaj1)

            self.brzina2 = np.add(self.brzina2 , b*self.dt)
            self.polozaj2 = np.add(self.polozaj2 , self.brzina2 * self.dt)
            self.polozaji2.append(self.polozaj2)

            self.dan = self.dan + 0.41

    def Runge_Kutta(self):
        while self.dan < self.vrijeme:
            akc1,akc2 = self.akc(0,0)
            k1vs = akc1 * self.dt
            k1s = np.dot(self.brzina1,self.dt)
            k1vz = akc2 * self.dt
            k1z = np.dot(self.brzina2,self.dt)

            akc1,akc2 = self.akc(k1s*0.5,0.5*k1z)
            k2vs = akc1 * self.dt
            k2s = (self.brzina1 + 0.5 * k1vs)*self.dt
            k2vz = akc2 * self.dt
            k2z = (self.brzina2 + 0.5 * k1vz)*self.dt

            akc1,akc2 = self.akc(k2s*0.5,0.5*k2z)
            k3vs = akc1 * self.dt
            k3s = (self.brzina1 + 0.5 * k2vs)*self.dt
            k3vz = akc2 * self.dt
            k3z = (self.brzina2 + 0.5 * k2vz)*self.dt

            akc1,akc2 = self.akc(k3s,k3z)
            k4vs = akc1 * self.dt
            k4s = (self.brzina1 + 0.5 * k3vs)*self.dt
            k4vz = akc2 * self.dt
            k4z = (self.brzina2 + 0.5 * k3vz)*self.dt

            self.brzina1 = self.brzina1 + (1/6)*(k1vs + 2 * k2vs + 2 * k3vs + k4vs)
            self.polozaj1 = self.polozaj1 + (1/6)*(k1s + 2 * k2s + 2 * k3s + k4s)
            self.polozaji1.append(self.polozaj1)

            self.brzina2 = self.brzina2 + (1/6)*(k1vz + 2 * k2vz + 2 * k3vz + k4vz)
            self.polozaj2 = self.polozaj2 + (1/6)*(k1z + 2 * k2z + 2 * k3z + k4z)
            self.polozaji2.append(self.polozaj2)

            self.dan = self.dan + 0.41
    def liste(self,a,b):
        x_list1 = []
        y_list1 = []
        z_list1 = []
        x_list2 = []
        y_list2 = []
        z_list2 = []

        for i in range(len(a)):
            x = a[i][0]
            y = a[i][1]
            z = a[i][2]
            x1 = b[i][0]
            y1 = b[i][1]
            z1 = b[i][2]
            x_list1.append(x)
            y_list1.append(y)
            z_list1.append(z)
            x_list2.append(x1)
            y_list2.append(y1)
            z_list2.append(z1)
        return x_list1,y_list1,z_list1,x_list2,y_list2,z_list2

    def plot_data(self):
        self.Runge_Kutta()
        x_suncerk,y_suncerk,z_suncerk,x_zemljark,y_zemljark,z_zemljark = self.liste(self.polozaji1,self.polozaji2)
        self.restart()
        self.Euler()
        x_sunce,y_sunce,z_sunce,x_zemlja,y_zemlja,z_zemlja = self.liste(self.polozaji1,self.polozaji2)
        return x_sunce,y_sunce,z_sunce,x_zemlja,y_zemlja,z_zemlja,x_zemljark,y_zemljark,z_zemljark

    def plot(self):
        x_sunce,y_sunce,z_sunce,x_zemlja,y_zemlja,z_zemlja,x_zemljark,y_zemljark,z_zemljark = self.plot_data()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        plt.plot(x_sunce, y_sunce, z_sunce, label="Sunce", c = 'y', marker='o')
        ax.scatter(x_sunce[0], y_sunce[0], z_sunce[0],s = 500, c = 'y')
        ax.scatter(x_zemlja, y_zemlja, z_zemlja, label="Zemlja Euler",s = 0.5 , c = 'black')
        ax.scatter(x_zemljark,y_zemljark,z_zemljark, label="Zemlja Runge-Kutta",s = 0.5 , c = 'm')
        ax.scatter(x_zemlja[0], y_zemlja[0], z_zemlja[0],s = 200, c = 'g')
        ax.set_xlabel('X-os')
        ax.set_ylabel('Y-os')
        ax.set_zlabel('Z-os')
        ax.legend()
        plt.show()   #Nema veće razlike između Rk i Eulerovoe metode za isti dt
          