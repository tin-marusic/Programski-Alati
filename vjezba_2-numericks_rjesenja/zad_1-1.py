import matplotlib.pyplot as plt 
import numpy as np


def jednoliko_gibanje(sila,masa):
    brzine = []
    polozaji = []
    akceleracije = []
    vremena = []

    n = 1000
    t = 10
    vrijeme = 0
    brzina = 0
    dt = t/n
    pomak = 0
    for i in range(n):
        akc = sila/masa
        brzina = brzina + akc*dt
        pomak = pomak + brzina*dt
        vrijeme = vrijeme + dt
        brzine.append(brzina)
        polozaji.append(pomak)
        akceleracije.append(akc)
        vremena.append(vrijeme)

    x_cord = [vremena]
    y_cord = [brzine]
    plt.subplot(3, 1, 1)
    plt.xlabel('vrijeme(s)')
    plt.ylabel('brzina(m/s)')
    plt.scatter(x_cord,y_cord,s=2)
    

    x_cord = [vremena]
    y_cord = [akceleracije]
    plt.subplot(3, 1, 2)
    plt.xlabel('vrijeme(s)')
    plt.ylabel('akceleracija(m/s**2)')
    plt.xlim([0,10])
    plt.ylim([0,akc + 2])
    plt.scatter(x_cord,y_cord,s=2)
    

    x_cord = [vremena]
    y_cord = [polozaji]
    plt.subplot(3, 1, 3)
    plt.scatter(x_cord,y_cord,s=2)
    plt.xlabel('vrijeme(s)')
    plt.ylabel('polozaj(m)')
    plt.show()

jednoliko_gibanje(5,5)