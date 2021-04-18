import math as m
import matplotlib.pyplot as plt
class Grafovi:
    def __init__(self,v0,masa,x0,k=0,cx = 0 ,s = 0 , Rho = 0):
        self.t1 = 0
        self.v = v0
        self.m = masa
        self.x0 = x0
        self.t = []
        self.x = []
        self.a = []
        self.brzine = []
        self.k = k
        self.Cx = cx
        self.s = s
        self.Rho = Rho
        self.sila1 = 0
        self.sila2 = 0
        self.sila3 = 0
        self.tocnost = False

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
        del self.Cx 
        del self.s 
        del self.sila2
        del self.sila3
        del self.sila1
        del self.tocnost

    def opis_gibanja(self,sila,dt , sila2 , sila3 ):
        t = self.t1
        v = self.v
        k = self.k
        x = self.x0
        g = 9.81
        m = self.m
        Cx = self.Cx
        S = self.s
        Rho = self.Rho 
        try:                               #provjerava jesu li vrijednosti tocno unesene
            self.sila1 = eval(sila)        # "uvrstava" vrijednosti u string i vraca numericku vrijednost
        except :
            self.tocnost = True             #prekida while petlju 
    
        try:
            if sila2 != 0:
                self.sila2 = eval(sila2)
        except :
            self.tocnost = True

        try:
            if sila3 != 0:
                self.sila3 = eval(sila3)
        except :
            self.tocnost = True

        sila1 = self.zbroj_sila()
        a = sila1/self.m
        self.v = self.v + a*dt
        self.x0 = self.x0 + self.v * dt
        self.t1 = self.t1 + dt
        self.t.append(self.t1)
        self.x.append(self.x0)
        self.a.append(a)
        self.brzine.append(self.v)


    def zbroj_sila(self):
        return self.sila1 + self.sila2 + self.sila3       #može se ubaciti beskonacno mnogo sila

    def crtanje(self,dt,sila,sila2 = 0,sila3 = 0 ):
        
        while self.tocnost == False:
            if self.t1>10:
                break
            else:
                if type(sila)==str: 
                    self.opis_gibanja(sila,dt,sila2,sila3)
                else:
                    print("Unjeli ste silu kao: ",type(sila))
                    print("Netočan unos,sila mora biti zadana u stringu!")
                    self.tocnost = True
                    

        if self.tocnost ==  False:          #crta grafove samo u slucaju kad su vrijednosti tocne
            x_cord = [self.t]
            y_cord = [self.x]
            plt.subplot(3, 1, 1)
            plt.scatter(x_cord,y_cord,s=1)
            plt.xlabel('vrijeme (s)')
            plt.ylabel('pomak (m)')

            x_cord = [self.t]
            y_cord = [self.brzine]
            plt.subplot(3, 1, 2)
            plt.scatter(x_cord,y_cord,s=1)
            plt.xlabel('vrijeme (s)')
            plt.ylabel('brzina (m/s)')

            x_cord = [self.t]
            y_cord = [self.a]
            plt.subplot(3, 1, 3)
            plt.scatter(x_cord,y_cord,s=1)
            plt.xlabel('vrijeme (s)')
            plt.ylabel('akceleracijia (m/s**2)')
            plt.show()
        else:
             print("Možete unositi samo predhodno definirane varijeble! Pazite na velika i mala slova!")