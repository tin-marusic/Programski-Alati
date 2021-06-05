import numpy as np
import math as m
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
 

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
        self.dio_dana = 0.417
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
        del self.dio_dana
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

            self.dan = self.dan + self.dio_dana

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
            self.dan = self.dan + self.dio_dana

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
        self.Runge_Kutta()
        x_sunce,y_sunce,z_sunce,x_zemlja,y_zemlja,z_zemlja = self.liste(self.polozaji1,self.polozaji2)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        plt.plot(x_sunce, y_sunce, z_sunce, label="Sunce", c = 'y', marker='o')
        ax.scatter(x_sunce[0], y_sunce[0], z_sunce[0],s = 500, c = 'y')
        ax.scatter(x_zemlja, y_zemlja, z_zemlja, label="Putanja zemlje",s = 0.5 , c = 'black')
        ax.scatter(x_zemlja[0], y_zemlja[0], z_zemlja[0],label="Zemlja",s = 200, c = 'g')
        ax.set_xlabel('X-os')
        ax.set_ylabel('Y-os')
        ax.set_zlabel('Z-os')
        ax.legend()
        max = plt.get_current_fig_manager()
        max.full_screen_toggle()       #za izlazak iz full screena stisnuti "ctrl + f" ,a za izlazak iz programa "ctrl + w"
        plt.show()   

    def anima(self):
        self.dio_dana = 1
        self.dt = 86400              #smanjuje broj točaka radi bržeg kretanja animacije
        self.vrijeme = self.vrijeme + 10
        def func(num, dataSet, lines):
            i = True
            for line, data in zip(lines, dataSet):
                line.set_data(data[0:2, :num])    
                line.set_3d_properties(data[2, :num])
                if i:
                    line.set_label("Putanja Zemlje Runge-Kutta")
                    line.set_color("w")
                    i = False
                else:
                    line.set_label("Putanja Zemlje Euler")
                legend = plt.legend()    
            return lines,legend
        x_sunce,y_sunce,z_sunce,x_zemlja,y_zemlja,z_zemlja,x_zemljark,y_zemljark,z_zemljark = self.plot_data()
        x_suncerk = np.array(x_sunce)
        y_suncerk = np.array(y_sunce)
        z_suncerk = np.array(z_sunce)
        x_zemljark = np.array(x_zemljark)
        y_zemljark = np.array(y_zemljark)
        z_zemljark = np.array(z_zemljark)
        dataSet = np.array([[x_zemljark,y_zemljark,z_zemljark],[x_zemlja,y_zemlja,z_zemlja]])

        numDataPoints = len(x_zemljark)
        fig = plt.figure()
        ax = Axes3D(fig)
        lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in dataSet]
        plt.rcParams['animation.html'] = 'html5'
        plt.axis('off')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_xlim(- 1.496E11, 1.496E11)
        ax.set_ylim(- 1.496E11, 1.496E11)
        ax.set_zlim(-1.1,1.1)
        ax.set_facecolor("black")
        ax.scatter(x_suncerk ,y_suncerk , z_suncerk ,label="Sunce",s = 500, c = 'y')
        line_ani = animation.FuncAnimation(fig, func, frames=numDataPoints, fargs=(dataSet,lines), interval=1, blit=False) 
        max = plt.get_current_fig_manager()
        max.full_screen_toggle()       #za izlazak iz full screena stisnuti "ctrl + f" ,a za izlazak iz programa "ctrl + w"

        plt.show()          #Nema veće razlike između Rk i Eulerovoe metode za isti dt

    def anima2(self):
        self.dio_dana = 1
        self.dt = 86400              #smanjuje broj točaka radi bržeg kretanja animacije
        self.vrijeme = self.vrijeme + 25 
        self.Euler()
        def func(num, dataSet, line):
            line.set_data(dataSet[0:2, :num])    
            line.set_3d_properties(dataSet[2, :num])
            line.set_label("Zemlja")
            line.set_marker("o")
            line.set_markersize(8)
            legend = plt.legend()    
            return line,legend
        x_suncerk,y_suncerk,z_suncerk,x_zemljark,y_zemljark,z_zemljark = self.liste(self.polozaji1,self.polozaji2)
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot(x_zemljark, y_zemljark, z_zemljark, label="Putanja zemlje", c = 'w')
        for i in range(3):   #smanjuje broj točaka u animaciji kako bi se mogla prikazati zemlja
            del x_zemljark[::2]
            del y_zemljark[::2]
            del z_zemljark[::2]
        x_suncerk = np.array(x_suncerk)
        y_suncerk = np.array(y_suncerk)
        z_suncerk = np.array(z_suncerk)
        x_zemljark = np.array(x_zemljark)
        y_zemljark = np.array(y_zemljark)
        z_zemljark = np.array(z_zemljark)
        dataSet = np.array([x_zemljark,y_zemljark,z_zemljark])

        numDataPoints = len(x_zemljark)
        
        line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='g')[0] 
        ax.set_facecolor("black")
        plt.axis('off')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.scatter(x_suncerk ,y_suncerk , z_suncerk ,label="Sunce",s = 500, c = 'y')
        line_ani = animation.FuncAnimation(fig, func, frames=numDataPoints, fargs=(dataSet,line), interval= 200, blit=False)
        max = plt.get_current_fig_manager()
        max.full_screen_toggle()       #za izlazak iz full screena stisnuti "ctrl + f" ,a za izlazak iz programa "ctrl + w"
        
        plt.show()