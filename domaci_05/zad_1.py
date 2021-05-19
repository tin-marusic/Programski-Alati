import numpy as np
import klasa as k
import matplotlib.pyplot as plt

p2 = k.Electromagnetic(0.4,0,0,0,1,np.array([0.1,0.1,0.1]),np.array([0,0,1]),np.array([0,0,0]))
p2.plot_usporedba()
p2.plot_elektron_pozitron()
p2.reset()