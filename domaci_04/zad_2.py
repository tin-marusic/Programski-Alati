import Projectile as p 
import matplotlib.pyplot as plt

p1 = p.Projectile(25,52,0.1,0,0,0.05,0.1,"kocka")
print(p1.plot_meta(1,15,5))
p1.reset()
