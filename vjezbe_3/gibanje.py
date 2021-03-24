import particle as prt

p1 = prt.particle(50,60,0,0)
print(p1.range(0.01))
p1.plot_trajectory()
p1.reset()