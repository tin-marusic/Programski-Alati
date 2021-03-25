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

    def total_time(self):
        dt = 0.001
        vrijeme = 0
        while True:
            self.vy = self.vy - 9.81*dt
            self.y0 = self.y0 + self.vy*dt
            if self.y0 > 0:
                vrijeme = vrijeme + dt
            else:
                break
        return vrijeme

    def max_speed(self):
        dt = 0.001
        brzina = self.vy
        while True:
            self.vy = self.vy - 9.81*dt
            self.y0 = self.y0 + self.vy*dt
            if self.y0 > 0:
                if abs(self.vy) > brzina:
                    brzina = self.vy
            else:
                break

        max = m.sqrt((self.vx)**2 + (brzina)**2)
        return max

    def velocity_to_hit_target(self,p,q,r):
        dt = 0.1
        v = 0.1
        epsilon = 0.1
        a = 0
        y = self.y0
        x = self.x0
        vx = v*m.cos(self.kut)
        vy = v*m.sin(self.kut)
        while True:
            vy = vy - 9.81*dt
            y = y + vy*dt
            if y > 0:
                x = x +  vx * dt
                udaljenost = ((x-p)**2) + ((y-q)**2)
                if udaljenost < (r**2 - epsilon):
                    a = 1
                    break
            else:
                y = self.y0
                x = self.x0
                v = v + 0.1
                vx = v*m.cos(self.kut)
                vy = v*m.sin(self.kut)

            if v > 100:
                print("Metu nije moguce pogoditi")
                break

        if a == 1:
            return v
            
    def angle_to_hit_target(self,p,q,r):
        v = self.v0
        dt = 0.1
        epsilon = 0.1
        a = 0
        stupnjevi = 0.1
        kut = (stupnjevi/180)*m.pi
        vx = v*m.cos(kut)
        vy = v*m.sin(kut)
        y = self.y0
        x = self.x0
        while True:
            vy = vy - 9.81*dt
            y = y + vy*dt
            if y > 0:
                x = x +  vx * dt
                udaljenost = ((x-p)**2) + ((y-q)**2)
                if udaljenost < (r**2 - epsilon):
                    a = 1
                    break
            else:
                y = self.y0
                x = self.x0
                stupnjevi = stupnjevi + 0.01
                kut = (stupnjevi/180)*m.pi
                vx = v*m.cos(kut)
                vy = v*m.sin(kut)

            if stupnjevi > 180:
                print("Metu nije moguce pogoditi")
                break

        if a == 1:
            return stupnjevi