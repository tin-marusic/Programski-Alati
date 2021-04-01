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
        return self.x , self.t

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
        omega = m.sqrt(10)
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
    
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        plt.plot(vrijeme,pomak_analiticki, c='b', label='analiticki')
        dt_02,vrijeme02 = self.opis_gibanja(0.5)
        #plt.plot(vrijeme02,dt_02, c='r',label='korak 0.5')
        ax1.scatter(vrijeme02,dt_02,s=5 , c='r',label='korak 0.5')
        self.reset()
        dt_01,vrijeme01 = self.opis_gibanja(0.25)
        plt.plot(vrijeme01, dt_01, c='g',label='korak 0.25')
        self.reset()
        dt_001,vrijeme001 = self.opis_gibanja(0.1)
        ax1.scatter(vrijeme001, dt_001, s=3.5, c='black',label='korak 0.1')
        self.reset()
        plt.xlabel('vrijeme (s)')
        plt.ylabel('pomak (m) ')
        plt.legend(loc='upper right')
        plt.title("Usporedba analitickog i numerickog rjesenja za razlicite korake")
        plt.show()