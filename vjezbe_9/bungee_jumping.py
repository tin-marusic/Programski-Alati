  
import matplotlib.pyplot as plt

class BungeeJumping:
    def __init__(self,y0,l0,k,m,rho = 1,Cd = 1.225,A = 1):
        self.y0 = y0
        self.y = y0
        self.polozaj = y0
        self.l0 = l0
        self.delta_l = 0
        self.konstanta = k
        self.masa = m
        self.gustoca = rho
        self.koeficjent = Cd
        self.povrsina = A
        self.polozaji = []
        self.vremena = []
        self.vy = 0
        self.dt = 0.001
        self.Ek = []
        self.Ep = []
        self.Ee = []
        self.energija = []

    def reset(self):
        del self.dt
        del self.y0
        del self.vy
        del self.y
        del self.polozaj
        del self.l0
        del self.konstanta
        del self.masa
        del self.gustoca
        del self.koeficjent
        del self.povrsina
        del self.delta_l
        del self.Ek
        del self.Ep
        del self.Ee
        self.polozaji.clear()
        self.vremena.clear()
        self.energija.clear()

    def povratak(self):
        del self.y
        self.polozaji.clear()
        self.vremena.clear()
        self.energija.clear()
        self.Ek.clear()
        self.Ep.clear()
        self.Ee.clear()
        self.vy = 0
        self.delta_l = 0
        self.y = self.y0
        self.polozaj = 0


    def elasticna_sila(self):
        if self.delta_l > 0:
            F = self.konstanta * self.delta_l
        else:
            F = 0
        return F 
    
    def otpor_zraka(self):
        if self.polozaj > self.y:         
            Fy = ((self.vy )**2 * self.povrsina * self.koeficjent * self.gustoca ) / 2   
        else:
            Fy = -(self.vy **2 * self.povrsina * self.koeficjent * self.gustoca ) / 2
        return Fy

    def kineticka(self):
        ek = (self.masa* (self.vy**2))/2
        self.Ek.append(ek)
        return ek

    def potencijalna(self):
        ep = self.masa * 9.81 * self.y
        self.Ep.append(ep)
        return ep

    def elasticna(self):
        ee = self.konstanta * self.delta_l**2 / 2
        self.Ee.append(ee)
        return ee

    def ukupna_energija(self):
        a = self.elasticna()
        b = self.kineticka()
        c = self.potencijalna()
        e = a + b + c 
        self.energija.append(e)
                
        
    def move_euler(self):
        t = 0
        while True:
            if t < 30:
                if self.y0 - self.y > self.l0:
                    self.delta_l = self.y0 - self.l0 - self.y 

                a = -9.81 + self.elasticna_sila()/self.masa
                self.vy = self.vy + a * self.dt
                self.y = self.y + self.vy * self.dt
                t = t + self.dt
                self.ukupna_energija()
                self.polozaji.append(self.y)
                self.vremena.append(t)
            else:
                break

    def move_euler_otpor(self):
        t = 0
        while True:
            if t < 30:
                if self.y0 - self.y > self.l0:
                    self.delta_l = self.y0 - self.l0 - self.y 

                a = -9.81 + (self.elasticna_sila()+self.otpor_zraka())/self.masa
                self.vy = self.vy + a * self.dt
                self.polozaj = self.y
                self.y = self.y + self.vy * self.dt
                t = t + self.dt
                self.ukupna_energija()
                self.polozaji.append(self.y)
                self.vremena.append(t)
            else:
                break

    def plot(self):
        self.move_euler()
        plt.plot(self.polozaji,self.vremena)
        plt.show()
        plt.plot(self.vremena,self.Ek,label = "Kineticka")
        plt.plot(self.vremena,self.Ep,label = "Potencijalna")
        plt.plot(self.vremena,self.Ee,label = "Elasticna")
        plt.plot(self.vremena,self.energija,label = "Ukupna")
        plt.legend()
        plt.show()

        self.povratak()

        self.move_euler_otpor()
        plt.plot(self.polozaji,self.vremena)
        plt.show()
        plt.plot(self.vremena,self.Ek,label = "Kineticka")
        plt.plot(self.vremena,self.Ep,label = "Potencijalna")
        plt.plot(self.vremena,self.Ee,label = "Elasticna")
        plt.plot(self.vremena,self.energija,label = "Ukupna")
        plt.legend()
        plt.show()
        