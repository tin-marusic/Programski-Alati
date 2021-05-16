import Projectile as p
import matplotlib.pyplot as plt

p1 = p.Projectile(8,51,0.14,0,0,0.035,0.1)
domet,koeficjenti = p1.domet_koeficjent()
plt.plot(domet,koeficjenti)
plt.xlabel('domet')
plt.ylabel('koeficjent')
plt.show()
p1.reset()

p2 = p.Projectile(8,51,0.14,0,0,0.035,0.1)
domet,masa = p2.masa_domet()
plt.plot(domet,masa)
plt.xlabel('domet')
plt.ylabel('masa')
plt.show()
p2.reset()
