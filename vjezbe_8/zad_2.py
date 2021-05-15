import Projectile as p
import matplotlib.pyplot as plt

p1 = p.Projectile(10,45,0.1,0,0,0.05,0.1)
p1.Euler_metoda()
x = p1.pomak_x
y = p1.pomak_y
plt.plot(x,y,label = "Eulerova metoda")

p1.varijable()

p1.Runge_Kutta()
x1 = p1.pomak_x
y1 = p1.pomak_y
plt.plot(x1,y1,label = "Runge_Kutta")
plt.legend()
plt.show()
p1.reset()