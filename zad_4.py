import matplotlib.pyplot as plt
import numpy as np

def kruznica(x,y,p,q,r):
    if (((x-p)**2) + ((y-q)**2) == r**2):
        print("Točka se nalazi na kružnici")
    elif (((x-p)**2) + ((y-q)**2) < r**2):
        print("Točka se nalazi unutar kružnice")
    else:
        print("Točka se nalazi van kružnice")
    
    kruznica = plt.Circle((p,q),r, color = "r")
    tocka = plt.Circle((x,y),0.2, color = "black")
    fig, ax = plt.subplots()
    ax.set_xlim((-r-5,r+5))
    ax.set_ylim((-r-5,r+5))
    ax.add_patch(kruznica)
    ax.add_patch(tocka)
    
    radnja = int(input("Unesite 1 ako želite vidjeti graf,a 2 ako želite spremiti graf. "))
    if radnja == 1:
        plt.show()
    if radnja == 2:
        naziv = input("Unesite naziv: ")
        plt.savefig(f"{naziv}.pdf")

kruznica(1.31,5.323,1.3143,0.31,5.24424)
