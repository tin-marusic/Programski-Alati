import matplotlib.pyplot as plt
import numpy as np
import rijecinci as r
import math as m
from matplotlib.animation import FuncAnimation

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
        self.size = (x["size"])

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


    def anima(self):
        fig = plt.figure(figsize = (5,5))
        axes = fig.add_subplot(111)
        axes.set_facecolor("black")
        x_liste = []
        y_liste = []
        for x in self.planeti:
            x_list = []
            y_list = []
            for i in range(len(x.x_y_z)):
                polozaj = x.x_y_z[i]
                x_list.append(polozaj[0])
                y_list.append(polozaj[1])
            axes.plot(x_list,y_list,c = x.c)
            for i in range(2):
                del x_list[::2]
                del y_list[::2]
            x_liste.append(x_list)
            y_liste.append(y_list)

        axes.scatter(0,0,s = 500, c = "y" , label = "Sunce")

        point, = axes.plot([x_liste[0][0]],[y_liste[0][0]], 'go')
        def ani(coords):
            point.set_data([coords[0]],[coords[1]])
            point.set_label(self.planeti[0].label)
            point.set_color(self.planeti[0].c)
            point.set_marker("o")
            point.set_markersize(self.planeti[0].size)
            legend = plt.legend()  
            return point,legend
        def frames():
            for acc_11_pos, acc_12_pos in zip(x_liste[0], y_liste[0]):
                yield acc_11_pos, acc_12_pos
        animation = FuncAnimation(fig, ani, frames=frames, interval=1)


        try:
            point1, = axes.plot([x_liste[1][0]],[y_liste[1][0]], 'go')
            def ani1(coords):
                point1.set_data([coords[0]],[coords[1]])
                point1.set_label(self.planeti[1].label)
                point1.set_color(self.planeti[1].c)
                point1.set_marker("o")
                point1.set_markersize(self.planeti[1].size)
                return point1
            def frames1():
                for acc_11_pos, acc_12_pos in zip(x_liste[1], y_liste[1]):
                    yield acc_11_pos, acc_12_pos
            animation1 = FuncAnimation(fig, ani1, frames=frames1, interval=1)
        except:
            pass

        try:
            point2, = axes.plot([x_liste[2][0]],[y_liste[2][0]], 'go')
            def ani2(coords):
                point2.set_data([coords[0]],[coords[1]])
                point2.set_label(self.planeti[2].label)
                point2.set_color(self.planeti[2].c)
                point2.set_marker("o")
                point2.set_markersize(self.planeti[2].size)
                return point2
            def frames2():
                for acc_11_pos, acc_12_pos in zip(x_liste[2], y_liste[2]):
                    yield acc_11_pos, acc_12_pos
            animation2 = FuncAnimation(fig, ani2, frames=frames2, interval=1)
        except:
            pass

        try:
            point3, = axes.plot([x_liste[3][0]],[y_liste[3][0]], 'go')
            def ani3(coords):
                point3.set_data([coords[0]],[coords[1]])
                point3.set_label(self.planeti[3].label)
                point3.set_color(self.planeti[3].c)
                point3.set_marker("o")
                point3.set_markersize(self.planeti[3].size)  
                return point3
            def frames3():
                for acc_11_pos, acc_12_pos in zip(x_liste[3], y_liste[3]):
                    yield acc_11_pos, acc_12_pos
            animation3 = FuncAnimation(fig, ani3, frames=frames3, interval=1)
        except:
            pass

        try:
            point4, = axes.plot([x_liste[4][0]],[y_liste[4][0]], 'go')
            def ani4(coords):
                point4.set_data([coords[0]],[coords[1]])
                point4.set_label(self.planeti[4].label)
                point4.set_color(self.planeti[4].c)
                point4.set_marker("o")
                point4.set_markersize(self.planeti[4].size)
                return point4
            def frames4():
                for acc_11_pos, acc_12_pos in zip(x_liste[4], y_liste[4]):
                    yield acc_11_pos, acc_12_pos
            animation4 = FuncAnimation(fig, ani4, frames=frames4, interval=1)

        except:
            pass

        maximum = plt.get_current_fig_manager()
        maximum.full_screen_toggle()       #za izlazak iz full screena stisnuti "ctrl + f" ,a za izlazak iz programa "ctrl + w"

        plt.show()