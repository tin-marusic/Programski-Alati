import math as m
import matplotlib.pyplot as plt
class Vertikalni_Hitac:
    def __init__(self,v0,h0):
        self.h0 = h0
        self.v0 = v0
        self.vrijeme = 0
        self.visine = []
        self.brzine = []
        self.vremena = []
        print("Objekt je uspješno stvoren!")
        print(f"Početna brzina je {self.v0} ,a visina {self.h0}.")

    def reset(self):
        del self.h0
        del self.v0

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


