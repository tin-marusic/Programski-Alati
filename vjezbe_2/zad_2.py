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
    vrijeme = (brzina_y*2) / 9.81
    domet = brzina_x * vrijeme
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

        else:
            polozaji_x.append(domet)
            polozaji_h.append(0)
        
    x_cord = [polozaji_x]
    y_cord = [polozaji_h]
    plt.scatter(x_cord,y_cord,s=2)
    plt.xlabel('domet(m)')
    plt.ylabel('visina(m)')
    plt.show()

    y_cord = [polozaji_x]
    x_cord = [vremena]
    plt.scatter(x_cord,y_cord, s=2)
    plt.xlabel('vrijeme(s)')
    plt.ylabel('domet(m)')
    plt.show()

    y_cord = [polozaji_h]
    x_cord = [vremena]
    plt.scatter(x_cord,y_cord, s=2)
    plt.xlabel('vrijeme(s)')
    plt.ylabel('visina(m)')
    plt.show()

