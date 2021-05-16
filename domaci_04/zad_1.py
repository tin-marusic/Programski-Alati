import Projectile as p 
import matplotlib.pyplot as plt

p1 = p.Projectile(8,51,0.14,0,0,0.035,0.1,"kugla")
x1,y1 = p1.izracun(0.11)
plt.plot(x1,y1,label = "kugla")

p2 = p.Projectile(8,51,0.14,0,0,0.035,0.1,"kocka")
x,y = p2.izracun(0.11)
plt.plot(x,y,label = "kocka")
plt.legend()
plt.show()
p1.reset()
p2.reset()