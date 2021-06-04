import zad_1 as z
import numpy as np

p2 = z.sun_earth(1.989E30, 5.972E24,np.array([0,0,0]),np.array([29780,0,0]),np.array([0,0,0]),np.array([0, 1.496E11,0]),365)
p2.plot()
p2.reset()