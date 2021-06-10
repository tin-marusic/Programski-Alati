import solar_sistem as z
import numpy as np

p1 = z.Universe("Sunce","Zemlja","Merkur","Venera","Mars")
p1.komet(10**14,np.array([-7500,-7500,0]),np.array([1.486E11,1.486E11*4.5,0]))
p1.anima()
p1.reset()

