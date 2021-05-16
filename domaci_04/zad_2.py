import Projectile as p 
import matplotlib.pyplot as plt

p1 = p.Projectile(25,52,0.1,0,0,0.05,0.1,"kocka")
print(p1.plot_meta(1,15,5))
p1.reset()

p1 = p.Projectile(25,52,0.1,0,0,0.05,0.1,"kocka")
print(p1.plot_meta(1,-25,6))
p1.reset()

p1 = p.Projectile(2500000,52,0.0000000001,0,0,10000,1000000,"kocka")
print(p1.plot_meta(0.1,0,10))
p1.reset()

p1 = p.Projectile(25,52,0.1,0,0,0.05,0.1,"kocka")
print(p1.plot_meta(0.5,0,10))
p1.reset()