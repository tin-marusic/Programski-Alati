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
        self.period = []

    def reset(self):
        self.t.clear()
        self.x.clear()
        self.brzine.clear()
        self.a.clear()

    def opis_gibanja(self,dt):
        self.period.clear()
        t = 0
        t1 = 0 
        v = self.v
        x = self.x0
        while True:
            if dt>0.05:
                if self.x0 - 0.5 < x and self.x0 + 0.5 > x:
                    t1 = t - t1
                    self.period.append(t1) 
            elif dt>0.009:
                if self.x0 - 0.02 < x and self.x0 + 0.02 > x:
                    t1 = t - t1
                    self.period.append(t1) 
            elif dt>0.001:
                if self.x0 - 0.005 < x and self.x0 + 0.005 > x:
                    t1 = t - t1
                    self.period.append(t1) 
            else: 
                if self.x0 - 0.0015< x and self.x0 + 0.0015 > x:
                    t1 = t - t1
                    self.period.append(t1)

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
        ax1.scatter(vrijeme001, dt_001, s=5, c='black',label='korak 0.1')
        self.reset()
        plt.xlabel('vrijeme (s)')
        plt.ylabel('pomak (m) ')
        plt.legend(loc='upper right')
        plt.title("Usporedba analitickog i numerickog rjesenja za razlicite korake")
        plt.show() 


    def period_titranja(self,dt):
        self.opis_gibanja(dt)
        try:
            period = 2*(self.period[1] - self.period[0]) 
        except:
            period = f"Period nije moguće izračunati za interval {dt}s!"
        return period
            
        

    def graf_prikaz(self,dt):
        x1 = (self.period_titranja(1))
        x2 = (self.period_titranja(0.5))
        x3 = (self.period_titranja(0.1))
        x4 = (self.period_titranja(0.01))
        x5 = (self.period_titranja(0.005))
        x6 = (self.period_titranja(0.001))
        x7 = (self.period_titranja(0.0005))
        period_analiticki = 2*m.pi * m.sqrt(self.m/self.k)

        fig = plt.figure() 
        column_labels=["dt (sekunde)", "Period (sekunde)"]
        data=[["Period analiticki",period_analiticki],
             [1,x1],
             [0.5,x2],
             [0.1,x3],
             [0.01,x4],
             [0.005,x5],
             [0.001,x6],
             [0.0005,x7]
             ]

        tablica = plt.table(cellText=data,
                            colWidths=[0.5] * 2 ,
                            colLabels=column_labels,
                            loc='center',
                            colColours =["yellow"] *2 )
        tablica.auto_set_font_size(False)
        tablica.set_fontsize(15)
        plt.show()

        promjena = dt
        pogreske = []
        vremena = []
        while dt<1:
            period = self.period_titranja(dt)
            if type(period) == float :
                greska = ((period - period_analiticki)/period_analiticki)*100
                pogreske.append(greska)
                vremena.append(dt)
            dt = dt + promjena

        plt.xlabel('vrijeme (s)')
        plt.ylabel('relativna pogreska(%) ')
        plt.plot(vremena,pogreske)
        plt.show()
