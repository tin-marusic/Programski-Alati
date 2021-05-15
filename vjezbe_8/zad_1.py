import Projectile as p 
import matplotlib.pyplot as plt

p2 = p.Projectile(10,45,0.1,0,0,0.05,0.1)
p2.Euler_metoda()
p2.plot()
p2.reset()

p1 = p.Projectile(10,45,0.1,0,0,0.05,0.1)
p1.Runge_Kutta()
p1.plot()
p1.reset()



