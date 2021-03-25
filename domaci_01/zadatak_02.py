import zadatak_01 as prt
import matplotlib.pyplot as plt

dometi = []
vremena = []
kutovi = []
t = 0
f = 0

for i in range (9000):
    p1 = prt.particle(10,t,0,0)
    d = p1.range(0.01)
    dometi.append(d)
    kutovi.append(t)
    t = t + 0.01

x_cord = [dometi]
y_cord = [kutovi]
plt.scatter(x_cord,y_cord,s=1)
plt.xlabel('domet (m)')
plt.ylabel('kut (°)')
plt.show()

for i in range (9000):
    p1 = prt.particle(10,f,0,0)
    d = p1.total_time()
    vremena.append(d)
    kutovi.append(f)
    f = f + 0.02

x_cord = [vremena]
y_cord = [kutovi[9000:18000]]
plt.scatter(x_cord,y_cord,s=1)
plt.xlabel('vrijeme(s)')
plt.ylabel('kut (°)')
plt.show()



