import kolokvij as kol
import math as m
import matplotlib.pyplot as plt

p1 = kol.Vertikalni_Hitac(10,10)
brzina,visina,vrijeme = p1.gibanje(0.01)
p1.reset()

def crtaj(h,v,t):
    plt.plot(t,h, c='b')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('pomak (m) ')
    plt.show()

    plt.plot(t,v, c='b')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('brzina (m/s) ')
    plt.show()

crtaj(visina,brzina,vrijeme)
