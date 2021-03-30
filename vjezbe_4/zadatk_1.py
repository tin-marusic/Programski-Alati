import calculus as c
import matplotlib.pyplot as plt

derivacije,lista_x = c.der2(c.f2,5,10,0.1,2)
derivacije_analiticki = []
lista_x2 = []
for e in lista_x:
    derivacija_analiticki = c.deriv_f2(e)
    derivacije_analiticki.append(derivacija_analiticki)
    lista_x2.append(e)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(lista_x,derivacije, s=1, c='b', label='numericki')
ax1.scatter(lista_x2,derivacije_analiticki, s=1, c='r',label='analiticki')
plt.xlabel('tocke')
plt.ylabel('iznos derivacje')
plt.legend(loc='upper left')
plt.title("Derivacija funkcije 5*x^3 - 2*x^2 + 2*x - 3")
plt.show()




derivacije,lista_x = c.der2(c.f4,5,10,0.1)
derivacije_analiticki = []
lista_x2 = []
for e in lista_x:
    derivacija_analiticki = c.deriv_f4(e)
    derivacije_analiticki.append(derivacija_analiticki)
    lista_x2.append(e)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(lista_x,derivacije, s=1, c='b', label='numericki')
ax1.scatter(lista_x2,derivacije_analiticki, s=1, c='r',label='analiticki')
plt.xlabel('tocke')
plt.ylabel('iznos derivacje')
plt.legend(loc='upper right')
plt.title("Derivacija funkcije sin(x) ")
plt.show()