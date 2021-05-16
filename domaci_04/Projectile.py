import math as m 
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,v0,kut,masa,x0,y0,A,Cx,Oblik,rho = 1.225,dt = 0.01):   #Gustoća zraka se može uzeti za konstantu
        kut = (kut/180)*m.pi
        self.kut = kut
        self.v0 = v0
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
        self.oblik = Oblik
        self.polozaj = y0
        self.polozaj_r = y0
        self.rho = rho 
        self.dt = dt
        self.pomak_x = [x0]
        self.pomak_y = [y0]

    def brisanje(self):
        del self.vx
        del self.vy
        del self.polozaj_x
        del self.polozaj_y
        del self.polozaj
        self.pomak_x.clear()
        self.pomak_y.clear()

    def reset(self):
        del self.v0
        del self.polozaj_r
        del self.polozaj
        del self.oblik
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

    def move_Runge_Kutta(self):
        if self.kut<m.pi/2:
            Fx = -(self.vx**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        else:                                               #Ukoliko se giba u smjeru -x osi sila će biti pozitivna
            Fx = (self.vx**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_x = Fx / self.masa
        k1vx = Akc_x * self.dt
        k1x = self.vx * self.dt
        if self.kut<m.pi/2:
            Fx = -((self.vx + 0.5*k1vx)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        else:
            Fx = ((self.vx + 0.5*k1vx)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_x = Fx / self.masa
        k2vx = Akc_x * self.dt
        k2x = (self.vx + 0.5 * k1vx) * self.dt
        if self.kut<m.pi/2:
            Fx = -((self.vx + 0.5*k2vx)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        else:
            Fx = ((self.vx + 0.5*k2vx)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_x = Fx / self.masa
        k3vx = Akc_x * self.dt
        k3x = (self.vx + 0.5 * k2vx) * self.dt
        if self.kut<m.pi/2:
            Fx = -((self.vx + 0.5*k3vx)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        else:
            Fx = ((self.vx + 0.5*k3vx)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_x = Fx / self.masa
        k4vx = Akc_x * self.dt
        k4x = (self.vx + k3vx) * self.dt
        self.vx = self.vx + (1/6)*(k1vx + 2 * k2vx + 2 * k3vx + k4vx)
        self.polozaj_x = self.polozaj_x + (1/6)*(k1x + 2 * k2x + 2 * k3x + k4x)
        self.pomak_x.append(self.polozaj_x)

        if self.polozaj > self.polozaj_y:         
            Fy = (self.vy**2 * self.povrsina * self.koeficjent * self.rho ) / 2   
        else:
            Fy = -(self.vy**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_y = Fy / self.masa - 9.81
        k1vy = Akc_y * self.dt
        k1y = self.vy * self.dt
        if self.polozaj > self.polozaj_y:         
            Fy = ((self.vy + 0.5* k1vy)**2 * self.povrsina * self.koeficjent * self.rho ) / 2   
        else:
            Fy = -((self.vy + 0.5* k1vy)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_y = Fy / self.masa - 9.81
        k2vy = Akc_y * self.dt
        k2y = (self.vy + 0.5 * k1vy) * self.dt
        if self.polozaj > self.polozaj_y:         
            Fy = ((self.vy + 0.5* k2vy)**2 * self.povrsina * self.koeficjent * self.rho ) / 2   
        else:
            Fy = -((self.vy + 0.5* k2vy)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_y = Fy / self.masa - 9.81
        k3vy = Akc_y * self.dt
        k3y = (self.vy + 0.5 * k2vy) * self.dt
        if self.polozaj > self.polozaj_y:         
            Fy = ((self.vy + 0.5* k3vy)**2 * self.povrsina * self.koeficjent * self.rho ) / 2   
        else:
            Fy = -((self.vy + 0.5* k3vy)**2 * self.povrsina * self.koeficjent * self.rho ) / 2
        Akc_y = Fy / self.masa - 9.81
        k4vy = Akc_y * self.dt
        k4y = (self.vy + k3vy) * self.dt
        self.vy = self.vy + (1/6)*(k1vy + 2 * k2vy + 2 * k3vy + k4vy)
        self.polozaj_y = self.polozaj_y + (1/6)*(k1y + 2 * k2y + 2 * k3y + k4y)
        self.pomak_y.append(self.polozaj_y)


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
        self.polozaj = self.polozaj_r
    
    def kugla(self,radijus):
        self.povrsina = radijus**2 *m.pi
        #kugla će uvijek u smjeru gibanja imati površinu jednaku površini kruga radijusa r na koje će djelovati sila
        #povrsina je jednaka i u x i y smjeru 
        x,y = self.Runge_Kutta()
        return x,y

    def kocka(self,brid):
        self.povrsina = brid**2
        #uvedena aproksimacija da se kocka ne rotira tijekom gibanja zbog čega će sila otpora
        #zraka uvijek djelovati na prednju plohu kocke (smjer gibanja) te na gornju ili donju 
        #plohu ovisno je li se giba u +y ili -y smjeru
        x1,y1 = self.Runge_Kutta()
        return x1,y1

    def izracun(self,osnovica):
        if self.oblik == "kugla":
            x,y = self.kugla(osnovica)
        elif self.oblik == "kocka":
            x,y = self.kocka(osnovica)
        try:
            return x,y
        except:
            print("Netočan unos")
            exit()

    def meta(self,radijus,xm,ym):

        v = self.v0
        dt = self.dt
        epsilon = 0.1
        izracun = False
        stupnjevi = 0.1
        kut = (stupnjevi/180)*m.pi
        self.kut = kut
        self.vx = v*m.cos(kut)
        self.vy = v*m.sin(kut)
        y = self.polozaj_y
        x = self.polozaj_x
        while True:
            self.move_Runge_Kutta()
            if self.polozaj_y > 0:
                udaljenost = ((self.polozaj_x-xm)**2) + ((self.polozaj_y-ym)**2)
                if radijus**2 < 0.25 :
                    if udaljenost < (radijus**2 - epsilon): #epsilon dodan kako bi se izbjegla granicna vrijednost
                        izracun = True
                        break
                else:
                    if udaljenost < radijus**2 :   #zbog premalog radijusa mora se ukloniti epsilon
                        izracun = True
                        break
            else:
                self.pomak_x.clear()
                self.pomak_y.clear()
                self.polozaj_y = y
                self.polozaj_x = x
                stupnjevi = stupnjevi + 0.1
                kut = (stupnjevi/180)*m.pi
                self.kut = kut
                self.vx = v*m.cos(kut)
                self.vy = v*m.sin(kut)

            if stupnjevi > 180:
                print("Metu nije moguce pogoditi")
                break
        

        if izracun == True:
            return stupnjevi

    def plot_meta(self,r,x,y):
        try:
            k = self.meta(r,x,y)
            if type(k)==float:
                kruznica = plt.Circle((x,y),r, color = "r")
                fig, ax = plt.subplots()
                ax.add_patch(kruznica)
                plt.plot(self.pomak_x,self.pomak_y,color = "b")
                plt.show()
                return k
        except OverflowError:
            #Ukoliko se unesu podaci koji za python daju prevelika rješenja smatra se da metu nije moguće pogoditi
            return "Metu nije moguće pogoditi"
            