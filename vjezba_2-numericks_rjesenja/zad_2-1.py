import matplotlib.pyplot as plt 
import numpy as np
from math import pi

def kosi_hitac(brzina,kut):
    polozaji_h = []
    polozaji_x = []
    vremena = []
    n = 2000
    t = 10
    vrijeme = 0
    dt = t/n
    polozaj_x = 0
    polozaj_y = 0
    kut = kut * pi / 180
    grav_konst = 9.81 
    brzina_y = np.sin(kut) * brzina
    brzina_x = np.cos(kut) * brzina
    for i in range(n):
        akc = grav_konst   #po potrebi se moze promijeniti u F/m ukoliko sila nije konstantna
        brzina_y = brzina_y - akc*dt
        polozaj_y = polozaj_y + brzina_y*dt
        vrijeme = vrijeme + dt
        vremena.append(vrijeme)
        if polozaj_y > 0 :
            polozaj_x = polozaj_x + brzina_x*dt
            polozaji_h.append(polozaj_y)
            polozaji_x.append(polozaj_x)
            
        else:
            domet = polozaj_x
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
