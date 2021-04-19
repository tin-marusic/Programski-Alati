import math as m
import matplotlib.pyplot as plt
class Vertikalni_Hitac:
    def __init__(self,v0,h0):
        self.h0 = h0
        self.v0 = v0
        self.vrijeme = 0
        self.visine = [h0]
        self.brzine = [v0]
        self.vremena = [0]
        self.polozaj  = 0
        print("Objekt je uspješno stvoren!")
        print(f"Početna brzina je {self.v0} ,a visina {self.h0}.")

    def reset(self):
        del self.h0
        del self.v0
        del self.vrijeme 
        self.visine.clear()
        self.brzine.clear()
        self.vremena.clear()
        del self.brzine 
        del self.vremena
        del self.polozaj

    def promjena_brzine(self,v):
        self.v0 = v
        return print(f"Nova brzina je {self.v0}.")

    def promjena_visine(self,h):
        self.h0 = h
        return print(f"Nova visina je {self.h0}.")

    def pomak(self,dt):
        akc = -9.81
        self.v0 = self.v0 + akc*dt 
        self.h0 = self.h0 + self.v0 * dt 
        self.vrijeme = self.vrijeme + dt
        self.visine.append(self.h0)
        self.brzine.append(self.v0)
        self.vremena.append(self.vrijeme)
        

    def gibanje(self,dt):
        while self.h0 > 0:
            self.pomak(dt)
        return self.brzine , self.visine , self.vremena

    def trajanje(self,dt):
        a,b,vrijeme = self.gibanje(dt)
        t = max(vrijeme)
        return t 

    def max_visina(self,dt):
        a,visina,vrijeme = self.gibanje(dt)
        h = max(visina)
        return h

    def otpor(self,dt,k,m):
        while self.h0 > 0:
            if  self.polozaj > self.h0:
                otpor_zraka = k*self.v0     #plus jer je gibanje u -y sjeru
            else:
                otpor_zraka = -k*self.v0    #minus jer je gibanje u +y sjeru
            sila_ukupna = m*-9.81 + otpor_zraka
            akc = sila_ukupna / m
            self.v0 = self.v0 + akc*dt 
            self.h0 = self.h0 + self.v0 * dt 
            print(self.h0)
            self.vrijeme = self.vrijeme + dt
            self.polozaj = self.h0
            self.visine.append(self.h0)
            self.brzine.append(self.v0)
            self.vremena.append(self.vrijeme)
        max_visina = max(self.visine)
        trajanje = max(self.vrijeme)
        return max_visina,trajanje
        
            

    


