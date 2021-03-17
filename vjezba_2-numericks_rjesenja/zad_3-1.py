import matplotlib.pyplot as plt 
import numpy as np
from math import pi

def kosi_hitac(brzina,kut):
    polozaji_h = []
    polozaji_x = []
    vremena = []
    n = 200000
    t = 100
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
        if polozaj_y > 0 :
            polozaji_h.append(polozaj_y)
            polozaj_x = polozaj_x +  brzina_x * dt
            polozaji_x.append(polozaj_x)
        else:
            break
        
    x_cord = [polozaji_x]
    y_cord = [polozaji_h]
    plt.scatter(x_cord,y_cord,s=2)
    plt.xlabel('domet(m)')
    plt.ylabel('visina(m)')
    plt.show()

def max_visina(brzina,kut):
    kut = kut * pi / 180
    n = 100000
    dt = 0.01
    grav_konst = 9.81
    polozaj_max = 0
    polozaj_y = 0
    brzina_y = np.sin(kut) * brzina
    for i in range(n):
        akc = grav_konst   #po potrebi se moze promijeniti u F/m ukoliko sila nije konstantna
        brzina_y = brzina_y - akc*dt
        polozaj_y = polozaj_y + brzina_y*dt
        if polozaj_y > polozaj_max:
            polozaj_max = polozaj_y
        else:
            print(f"najveca visina je: {polozaj_max}")
            break

def domet(brzina,kut):
    kut = kut * pi / 180
    brzina_y = np.sin(kut) * brzina
    brzina_x = np.cos(kut) * brzina
    n = 100000
    dt = 0.01
    grav_konst = 9.81
    polozaj_max_x = 0
    polozaj_y = 0

    for i in range(n):
        akc = grav_konst   #po potrebi se moze promijeniti u F/m ukoliko sila nije konstantna
        brzina_y = brzina_y - akc*dt
        polozaj_y = polozaj_y + brzina_y*dt
        if polozaj_y > 0:
            polozaj_max_x = polozaj_max_x + brzina_x*dt
        else:
            print(f"najveca domet je: {polozaj_max_x}")
            break

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
    n = 1000000
    dt = 0.0001 #jako puno djelica da se dobije preciznija slika
    grav_konst = 9.81
    polozaj_y = 0
    polozaj_x = 0
    epsilon = 0.1
    a = 0

    for i in range(n):
        akc = grav_konst
        brzina_y = brzina_y - akc*dt
        polozaj_y = polozaj_y + brzina_y*dt
        if polozaj_y > 0:
            polozaj_x = polozaj_x +  brzina_x * dt
            polozaji_h.append(polozaj_y)
            polozaji_x.append(polozaj_x)
            udaljenost = ((polozaj_x-p)**2) + ((polozaj_y-q)**2)
            if udaljenost < (radijus**2 + epsilon):
                print("meta je pogođena")
                a = 1
                break
            else:
                udaljenost = np.sqrt(udaljenost) - (radijus)
                udaljenosti.append(udaljenost)
        else:
            break  #izlazak iz for petlje kako se bi ponavljala nepotrebno puno puta

    if a==0 :
        udaljenosti.sort()
        print(f"Najmanja udaljenost je {udaljenosti[0]}")
        

    x_cord = [polozaji_x]
    y_cord = [polozaji_h]
    kruznica = plt.Circle((p,q),radijus, color = "r")
    fig, ax = plt.subplots()
    ax.add_patch(kruznica)
    plt.scatter(x_cord,y_cord,s=1)
    plt.xlabel('domet(m)')
    plt.ylabel('visina(m)')
    plt.show()
    
    



