import math as m
import matplotlib.pyplot as plt
class HarmonicOscillator:
    def __init__(self,v0,masa,konstanta,x0):
        self.v = v0
        self.m = masa
        self.k = konstanta
        self.x0 = x0
        self.t = []
        self.x = []
        self.a = []
        self.brzine = []

    def reset(self):
        self.t.clear()
        self.x.clear()
        self.brzine.clear()
        self.a.clear()

    def opis_gibanja(self,dt):
        t = 0
        v = self.v
        x = self.x0
        while True:
            a = (-self.k*x)/self.m
            v = v + a*dt
            x = x + v * dt
            t = t + dt
            self.t.append(t)
            self.x.append(x)
            self.a.append(a)
            self.brzine.append(v)
            if t>10:
                break

    def plot(self,dt):
        self.opis_gibanja(dt)
        x_cord = [self.t]
        y_cord = [self.x]
        plt.scatter(x_cord,y_cord,s=1)
        plt.xlabel('vrijeme (s)')
        plt.ylabel('pomak (m)')
        plt.show()

        x_cord = [self.t]
        y_cord = [self.brzine]
        plt.scatter(x_cord,y_cord,s=1)
        plt.xlabel('vrijeme (s)')
        plt.ylabel('brzina (m/s)')
        plt.show()

        x_cord = [self.t]
        y_cord = [self.a]
        plt.scatter(x_cord,y_cord,s=1)
        plt.xlabel('vrijeme (s)')
        plt.ylabel('akceleracijia (m/s**2)')
        plt.show()


    def analiticko_rjesenje(self,dt):
        pomak_analiticki = []
        vrijeme = []
        vrijeme001 = []
        vrijeme01 = []
        dt_01 = []
        omega = m.sqrt(0.1)
        amp = 1
        vrije = 0
        while True:
            vrije = vrije + dt
            x = amp * m.sin(omega * vrije)
            pomak_analiticki.append(x)
            vrijeme.append(vrije)
            if vrije>10:
                break
        self.reset()
        self.opis_gibanja(0.01)
        dt_001 = self.x
        vrijeme001 = self.t
        self.reset()
        self.opis_gibanja(0.1)
        vrijeme01 = self.t
        dt_01.append(self.x )
        self.reset()
        self.opis_gibanja(1)
        dt_1 = self.x

        print(dt_01)
        print(dt_1)

        
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        plt.plot(vrijeme,pomak_analiticki, c='b', label='analiticki')
        plt.plot(vrijeme001, dt_001, c='r',label='numericki')
        plt.plot(vrijeme01, dt_01, c='g',label='numericki')
        #plt.plot(self.t, dt_1, c='black',label='numericki')
        plt.xlabel('vrijeme')
        plt.ylabel('pomak')
        #plt.legend(loc='upper left')
        plt.show()