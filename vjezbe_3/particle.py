import math as m 
import matplotlib.pyplot as plt

class particle:
    def __init__(self,v0,kut,x0,y0):
        self.v0 = v0
        kut = (kut/180)*m.pi
        self.kut = kut
        self.x0 = x0
        self.y0 = y0
        self.vx = self.v0*m.cos(self.kut)
        self.vy = self.v0*m.sin(self.kut)
        self.pomak_x = []
        self.pomak_y = []

    def reset(self):
        del self.v0
        del self.kut
        del self.x0
        del self.y0
        del self.vx
        del self.vy
        del self.pomak_x
        del self.pomak_y

    def __move(self,dt):
        self.vy = self.vy - 9.81*dt
        self.x0 = self.x0 + self.vx * dt
        self.pomak_x.append(self.x0)
        self.y0 = self.y0 + self.vy * dt
        self.pomak_y.append(self.y0)

    def range(self,dt):
        pocetni_polozaj = self.x0
        while True:
            self.__move(dt)
            if self.y0 <= 0:
                break
        domet = self.pomak_x[-1] - pocetni_polozaj
        return domet

    def plot_trajectory(self):
        x_cord = [self.pomak_x]
        y_cord = [self.pomak_y]
        plt.scatter(x_cord,y_cord,s=1)
        plt.xlabel('domet(m)')
        plt.ylabel('visina(m)')
        plt.show()
