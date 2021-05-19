import numpy as np
import electromagnetic_field as em
import matplotlib.pyplot as plt

p2 = em.Electromagnetic(1,0,0,0,1,np.array([0.1,0.1,0.1]),np.array([0,0,1]),np.array([0,0,0]))
p2.plot()
p2.reset()


