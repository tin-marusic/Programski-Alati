import zad_1 as z
import numpy as np

p1 = z.Universe("Sunce","Zemlja","Merkur","Venera","Mars")
p1.plot()
p1.anima()
p1.reset()

p1 = z.Universe("Sunce","Venera","Mars")
p1.plot()
p1.anima()
p1.reset()


p1 = z.Universe("Venera","Sunce","Merkur","Mars","Zemlja")
p1.plot()
p1.anima()
p1.reset()
