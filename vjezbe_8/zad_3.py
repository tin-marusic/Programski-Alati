import Projectile as p
import matplotlib.pyplot as plt

p1 = p.Projectile(10,45,0.1,0,0,0.05,0.1)
domet,koeficjenti = p1.domet_koeficjent()
plt.plot(domet,koeficjenti)
plt.xlabel('domet')
plt.ylabel('koeficjent')
plt.show()
p1.reset()

p2 = p.Projectile(10,45,0.1,0,0,0.05,0.1)
domet,masa = p2.masa_domet()
plt.plot(domet,masa)
plt.xlabel('domet')
plt.ylabel('koeficjent')
plt.show()
p2.reset()
