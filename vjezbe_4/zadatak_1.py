import calculus as c
import matplotlib.pyplot as plt
import numpy as np

derivacije,lista_x = c.der2(c.f2,5,10,0.1,2)
derivacije_analiticki = []
for e in range (1002):
    tocke = np.linspace(lista_x[0],lista_x[-1],1002)
    derivacija_analiticki = c.deriv_f2(tocke[e])
    derivacije_analiticki.append(derivacija_analiticki)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.scatter(lista_x,derivacije, s=3, c='b', label='numericki')
ax1.plot(tocke,derivacije_analiticki,c='r',label='analiticki')
plt.xlabel('tocke')
plt.ylabel('iznos derivacje')
plt.legend(loc='upper left')
plt.title("Derivacija funkcije 5*x^3 - 2*x^2 + 2*x - 3")
plt.show()




derivacije,lista_x = c.der2(c.f4,5,10,0.1)
derivacije_analiticki = []
for e in range (1002):
    tocke = np.linspace(lista_x[0],lista_x[-1],1002)
    derivacija_analiticki = c.deriv_f4(tocke[e])
    derivacije_analiticki.append(derivacija_analiticki)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(tocke,derivacije_analiticki, c='y',label='analiticki')
ax1.scatter(lista_x,derivacije, s=3.5, c='black', label='numericki')
plt.xlabel('tocke')
plt.ylabel('iznos derivacje')
plt.legend(loc='upper right')
plt.title("Derivacija funkcije sin(x) ")
plt.show()