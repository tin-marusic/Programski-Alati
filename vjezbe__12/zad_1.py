import matplotlib.pyplot as plt
import numpy as np
import rijecinci as r
import math as m

class Planets:
    def __init__(self, x):
        self.v = (x["brzina"])
        self.m = (x["masa"])
        self.x = (x["polozaj"])
        self.s = (x["velicina"])
        self.label = (x["ime"])
        self.c = (x["boja"])
        self.x_y_z = [self.x]
        self.akceleracija = np.array([0,0,0])

class Universe:
    def __init__(self, x,y,z=0,j=0,k=0):
        tijela1 = [x,y,z,j,k]
        tijela2 = ["Sunce","Merkur","Venera","Zemlja","Mars"]
        self.planeti = []
        for i in range (5):
            x = tijela1[i]
            if x==tijela2[0]:
                p1 = Planets(r.sunce)
                self.planeti.append(p1)
            elif x==tijela2[1]:
                p1 = Planets(r.merkur)
                self.planeti.append(p1)
            elif x==tijela2[2]:
                p1 = Planets(r.venera)
                self.planeti.append(p1)
            elif x==tijela2[3]:
                p1 = Planets(r.zemlja)
                self.planeti.append(p1)
            elif x==tijela2[4]:
                p1 = Planets(r.mars)
                self.planeti.append(p1)

    def reset(self):
        del self.planeti

    def calculate(self):
        G = 6.67408E-11
        t = 0
        T = 5 * 365 * 24 * 3600
        dt = 36000
        while t<T:
            for x in self.planeti:
                for y in self.planeti:
                    if x!=y:
                        udaljenost = np.linalg.norm(abs(np.subtract(x.x,y.x)))**3
                        akc1 = -G * (y.m * (np.subtract(x.x,y.x))/ udaljenost)
                        for i in range(3):
                            if m.isnan(akc1[i])==True:
                                akc1[i ]= 0
                        x.akceleracija = np.add(akc1,x.akceleracija)
            for x in self.planeti:
                x.v1 = np.add(x.v,x.akceleracija*dt)
                x.x = np.add(x.x , x.v1 * dt)
                x.x_y_z.append(x.x)
            t = t + dt

    def plot(self):
        self.calculate()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for x in self.planeti:
            x_list = []
            y_list = []
            z_list = []
            for i in range(len(x.x_y_z)):
                polozaj = x.x_y_z[i]
                x_list.append(polozaj[0])
                y_list.append(polozaj[1])
                z_list.append(polozaj[2])
            ax.scatter(x_list[-1],y_list[-1],z_list[-1],s = x.s, c = x.c , label = x.label)
            plt.plot(x_list, y_list, z_list, c = x.c)
        ax.set_facecolor("black")
        ax.legend()
        plt.axis('off')
        ax.set_xticks([])         
        ax.set_yticks([])
        ax.set_zticks([])
        max = plt.get_current_fig_manager()
        max.full_screen_toggle()       #za izlazak iz full screena stisnuti "ctrl + f" ,a za izlazak iz programa "ctrl + w"
        plt.show()   
