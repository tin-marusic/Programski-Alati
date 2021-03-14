import matplotlib.pyplot as plt 
import numpy as np
from math import pi

def kosi_hitac(brzina,kut):
    polozaji_h = []
    polozaji_x = []
    vremena = []

    kut = kut * pi / 180
    brzina_y = np.sin(kut) * brzina
    brzina_x = np.cos(kut) * brzina
    t = 10/(1500)
    x = 0
    for i in range (1500):
        x = x + t
        vremena.append(x)
        polozaj_h = (brzina_y * x) - (9.81 * (x**2) / 2)
        if polozaj_h > 0 :
            polozaji_h.append(polozaj_h)
            polozaj_x =  brzina_x * x
            polozaji_x.append(polozaj_x)
        
    x_cord = [polozaji_x]
    y_cord = [polozaji_h]
    plt.scatter(x_cord,y_cord,s=2)
    plt.xlabel('domet(m)')
    plt.ylabel('visina(m)')
    plt.show()

def max_visina(brzina,kut):
    kut = kut * pi / 180
    brzina_y = np.sin(kut) * brzina
    max_visina1 = (brzina_y**2)/(2*9.81)
    return max_visina1 

def domet(brzina,kut):
    kut = kut * pi / 180
    brzina_y = np.sin(kut) * brzina
    brzina_x = np.cos(kut) * brzina
    vrijeme = (brzina_y*2) / 9.81
    domet = brzina_x * vrijeme
    return domet

def max_brzina(brzina,kut):
    max_brzina = brzina  #maksimalna brzina će biti jednaka početnoj ako tijekom gibanja na tijelo ne djeluje neka dodatna sila
    return max_brzina


def meta(brzina,kut,radijus,p,q):
    polozaji_h = []
    polozaji_x = []
    udaljenosti = []
    kut = kut * pi / 180
    brzina_y = np.sin(kut) * brzina
    brzina_x = np.cos(kut) * brzina
    vrijeme = (brzina_y*2) / 9.81

    t = vrijeme/(10000)
    x = 0
    y = 0
    epsilon = 0.01
    
    for i in range(10000):
        x = x + t
        polozaj_h = (brzina_y * x) - (9.81 * (x**2) / 2)
        if polozaj_h > 0 :
            polozaj_x =  brzina_x * x
            udaljenost = ((polozaj_x-p)**2) + ((polozaj_h-q)**2) 
            if udaljenost < (radijus**2 + epsilon):
                print("meta je pogođena")
                break
            else:
                udaljenost = udaljenost - (radijus**2)
                udaljenosti.append(udaljenost)
    if len(udaljenosti)==9999:
        udaljenosti.sort()
        print(f"Najmanja udaljenost je {udaljenosti[0]}")

    for e in range (10000):
        y = y + t
        polozaj_h = (brzina_y * y) - (9.81 * (y**2) / 2)
        if polozaj_h > 0 :
            polozaji_h.append(polozaj_h)
            polozaj_x =  brzina_x * y
            polozaji_x.append(polozaj_x)
        
    x_cord = [polozaji_x]
    y_cord = [polozaji_h]
    kruznica = plt.Circle((p,q),radijus, color = "r")
    fig, ax = plt.subplots()
    ax.add_patch(kruznica)
    plt.scatter(x_cord,y_cord,s=2)
    plt.xlabel('domet(m)')
    plt.ylabel('visina(m)')
    plt.show()

