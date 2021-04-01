import math as m
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self,v0,masa,x0):
        self.t1 = 0
        self.v = v0
        self.m = masa
        self.x0 = x0
        self.t = []
        self.x = []
        self.a = []
        self.brzine = []
        self.k = 0
        self.g = 0
        self.Cx = 0
        self.s = 0
        self.Rho = 0
        self.ime = 0
        self.ime1 = 0
        self.ime2 = 0
        self.sila1 = 0
        self.sila2 = 0
        self.sila3 = 0

    def reset(self):
        self.t.clear()
        self.x.clear()
        self.brzine.clear()
        self.a.clear()
        del self.t1
        del self.v
        del self.m
        del self.x0
        del self.k
        del self.g
        del self.Cx 
        del self.s 
        del self.ime
        del self.ime1
        del self.ime2 
        del self.sila2
        del self.sila3
        del self.sila1

    def opis_gibanja(self,sila,dt):
            a = (sila)/self.m
            self.v = self.v + a*dt
            self.x0 = self.x0 + self.v * dt
            self.t1 = self.t1 + dt
            self.t.append(self.t1)
            self.x.append(self.x0)
            self.a.append(a)
            self.brzine.append(self.v)

    def elasticna_sila(self , k):
        self.k = k
        self.ime = 1
        self.sila1 = -k*self.x0
        return -k*self.x0

    def  gravitacijska_sila(self,g):
        self.ime1 = 1
        self.g = g
        self.sila2 = self.m * g
        return self.m * g

    def otpor_zraka(self,Cx,S,Rho):
        self.Cx = Cx
        self.s = S
        self.Rho = Rho
        self.ime2 = 1
        a = -Cx*S*((Rho*(self.v**2))/2)   #minus jer ce otpor zraka uvijek bit suprotan od gibanja tijela
        self.sila3 = a
        return a

    def zbroj_sila(self):
        return self.sila1 + self.sila2 + self.sila3       #može se ubaciti beskonacno mnogo sila

    def plot(self,dt,sila,sila2 = 0,sila3 = 0 ):
        while True:
            if self.t1>10:
                break
            else:
                if self.ime == 1:
                    self.elasticna_sila(self.k)
                elif self.ime1 == 1 and self.ime2 == 1:
                    self.gravitacijska_sila(self.g)
                    self.otpor_zraka(self.Cx , self.s , self.Rho)           #lako se ubaci jos jedan uvjet ako se doda jos jedna sila
                elif self.ime1 == 1:
                    self.gravitacijska_sila(self.g)
                elif self.ime2 == 1:
                    self.otpor_zraka(self.Cx , self.s , self.Rho)
                sila = self.zbroj_sila()
                self.opis_gibanja(sila,dt)

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
