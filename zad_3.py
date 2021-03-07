import matplotlib.pyplot as plt
import numpy as np

def pravac(x,y,x2,y2):

    nagib = (y2-y)/(x2-x)
    nagib = round(nagib,3)
    sl_koeficjent = -x*nagib + y
    if sl_koeficjent>0:
        sl_koeficjent = str(sl_koeficjent)
        sl_koeficjent = "+ " + sl_koeficjent
    print (f"y = {nagib}x {sl_koeficjent}")

    xpoints = np.array([x,x2])
    ypoints = np.array([y,y2])
    plt.scatter(x,y)
    plt.scatter(x2,y2)
    plt.plot(xpoints, ypoints)
    
    radnja = int(input("Unesite 1 ako želite vidjeti graf,a 2 ako želite spremiti graf. "))
    if radnja == 1:
        plt.show()
    if radnja == 2:
        naziv = input("Unesite naziv: ")
        plt.savefig(f"{naziv}.pdf")
        
pravac(12,23,11,64)