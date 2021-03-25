import particle as prt
import math as m 
import matplotlib.pyplot as plt

def domet_analiticki(v0,kut,y0):
    kut = (kut/180)*m.pi
    vx = v0*m.cos(kut)
    vy = v0*m.sin(kut)
    vrijeme = (vy + m.sqrt(vy**2 + 2*9.81*y0))/9.81
    dometanaliticki = vx * vrijeme 
    return dometanaliticki 


def relativna_pogreska():
    pogreska_postotak = []
    vremena = []
    dt = 0
    promjena = 0.0001
    t = domet_analiticki(10,60,0)
    
    for i in range(10000):
        dt = dt + promjena
        p1 = prt.particle(10,60,0,0)
        pogreska = abs(((p1.range(dt)-t)/t)*100)
        p1.reset()
        vremena.append(dt)
        pogreska_postotak.append(pogreska)
    p1 = prt.particle(10,60,0,0)
    print(p1.range(0.0001))
    print(pogreska_postotak[0])
    x_cord = [vremena]
    y_cord = [pogreska_postotak]
    plt.scatter(x_cord,y_cord,s=0.2)
    plt.xlabel('iznos vremena dt')
    plt.ylabel('pogreška u %')
    plt.show()

    plt.plot(vremena[0:10000:100],pogreska_postotak[0:10000:100]) #manje točan crtež,ali pregledniji u ovom slucaju
    plt.xlabel('iznos vremena dt')
    plt.ylabel('pogreška u %')
    plt.show()


relativna_pogreska()
