import math as m 
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,v0,kut,masa,x0,y0,A,Cx,rho = 1.225,dt = 0.01):   #Gustoća zraka se može uzeti za konstantu
        kut = (kut/180)*m.pi
        self.kut = kut
        self.vx = v0*m.cos(self.kut)
        self.vxr = v0*m.cos(self.kut)
        self.vy = v0*m.sin(self.kut)
        self.vyr = v0*m.sin(self.kut)
        self.masa = masa
        self.polozaj_x = x0
        self.polozaj_x_r = x0
        self.polozaj_y = y0
        self.polozaj_y_r = y0 
        self.povrsina = A
        self.koeficjent = Cx
        self.rho = rho 
        self.dt = dt
        self.pomak_x = [x0]
        self.pomak_y = [y0]

    def brisanje(self):
        del self.vx
        del self.vy
        del self.polozaj_x
        del self.polozaj_y
        self.pomak_x.clear()
        self.pomak_y.clear()

    def reset(self):
        del self.kut
        del self.vx
        del self.vy
        del self.masa
        del self.polozaj_x
        del self.polozaj_y
        del self.povrsina
        del self.koeficjent
        del self.rho
        del self.dt
        del self.polozaj_x_r
        del self.polozaj_y_r
        del self.vxr
        del self.vyr
        self.pomak_x.clear()
        self.pomak_y.clear()

    def move_euler(self,dt):
        Fx = -(self.vx**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_x = Fx / self.masa
        self.vx = self.vx + Akc_x*dt
        self.polozaj_x = self.polozaj_x + self.vx * dt
        self.pomak_x.append(self.polozaj_x)

        Fy = -(self.vy**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        #pretpostavka da je tijelo pravilno tako da je povrsina u x i y smjeru jednaka
        Akc_y = Fy / self.masa
        self.vy = self.vy - 9.81*dt + Akc_y*dt
        self.polozaj_y = self.polozaj_y + self.vy * dt
        self.pomak_y.append(self.polozaj_y)

    def move_Runge_Kutta(self):
        Fx = -(self.vx**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_x = Fx / self.masa
        k1vx = Akc_x * self.dt
        k1x = self.vx * self.dt
        Fx = -((self.vx + 0.5*k1vx)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_x = Fx / self.masa
        k2vx = Akc_x * self.dt
        k2x = (self.vx + 0.5 * k1vx) * self.dt
        Fx = -((self.vx + 0.5*k2vx)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_x = Fx / self.masa
        k3vx = Akc_x * self.dt
        k3x = (self.vx + 0.5 * k2vx) * self.dt
        Fx = -((self.vx + 0.5*k3vx)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_x = Fx / self.masa
        k4vx = Akc_x * self.dt
        k4x = (self.vx + k3vx) * self.dt
        self.vx = self.vx + (1/6)*(k1vx + 2 * k2vx + 2 * k3vx + k4vx)
        self.polozaj_x = self.polozaj_x + (1/6)*(k1x + 2 * k2x + 2 * k3x + k4x)
        self.pomak_x.append(self.polozaj_x)

        Fy = -(self.vy**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_y = Fy / self.masa - 9.81
        k1vy = Akc_y * self.dt
        k1y = self.vy * self.dt
        Fy = -((self.vy + 0.5* k1vy)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_y = Fy / self.masa - 9.81
        k2vy = Akc_y * self.dt
        k2y = (self.vy + 0.5 * k1vy) * self.dt
        Fy = -((self.vy + 0.5* k2vy)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_y = Fy / self.masa - 9.81
        k3vy = Akc_y * self.dt
        k3y = (self.vy + 0.5 * k2vy) * self.dt
        Fy = -((self.vy + 0.5* k3vy)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_y = Fy / self.masa - 9.81
        k4vy = Akc_y * self.dt
        k4y = (self.vy + k3vy) * self.dt
        self.vy = self.vy + (1/6)*(k1vy + 2 * k2vy + 2 * k3vy + k4vy)
        self.polozaj_y = self.polozaj_y + (1/6)*(k1y + 2 * k2y + 2 * k3y + k4y)
        self.pomak_y.append(self.polozaj_y)


    def Euler_metoda(self):
        while True:
            self.move_euler(self.dt)
            if self.polozaj_y <= 0:
                break
        return self.pomak_x,self.pomak_y

    def Runge_Kutta(self):
        while True:
            self.move_Runge_Kutta()
            if self.polozaj_y <= 0:
                break
        return self.pomak_x,self.pomak_y

    def varijable(self):
        self.brisanje()
        self.vx = self.vxr
        self.vy = self.vyr
        self.polozaj_x = self.polozaj_x_r
        self.polozaj_y = self.polozaj_y_r
    
    def domet(self):
        x0 = self.polozaj_x
        while True:
            self.Runge_Kutta()
            if self.polozaj_y <= 0:
                break
        domet = abs(self.polozaj_x - x0)
        self.varijable()
        return domet

    def domet_koeficjent(self):
        self.koeficjent = 0
        dometi = []
        koeficjenti = []
        for i in range(1000):
            d = self.domet()
            dometi.append(d)
            koeficjenti.append(self.koeficjent)
            self.koeficjent = self.koeficjent + 0.01
        return dometi,koeficjenti

    def masa_domet(self):
        self.masa = 0.01
        dometi = []
        mase = []
        for i in range(1000):
            d = self.domet()
            dometi.append(d)
            mase.append(self.masa)
            self.masa = self.masa + 0.01
        return dometi,mase

    def plot(self):
        plt.plot(self.pomak_x,self.pomak_y)
        plt.show()

