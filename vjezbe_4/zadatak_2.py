import calculus as c
import matplotlib.pyplot as plt

iznosi_pravkutno_donji = []
iznosi_pravkutno_gornji = []
iznosi_trapezno = []
iznosi_analiticki = []
broj_podjela = []
for i in range (19):
    if i > 0:
        broj_podjela.append(i)

        g,d = c.integral_pravokutnik(c.f1,8,15,i)
        iznosi_pravkutno_gornji.append(g)
        iznosi_pravkutno_donji.append(d)

        iznos_trapezno = c.integral_trapez(c.f1,8,15,i)
        iznosi_trapezno.append(iznos_trapezno)

        iznos_analiticki = c.integ_f1(15) - c.integ_f1(8)
        iznosi_analiticki.append(iznos_analiticki)


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.plot(broj_podjela,iznosi_pravkutno_donji,c='b',linewidth = 1, label='numericki pravokutno donje međe')
plt.plot(broj_podjela,iznosi_pravkutno_gornji,c='m',linewidth = 1, label='numericki pravokutno gornje međe')
plt.plot(broj_podjela,iznosi_trapezno,c='r',label='numericki trapezno')
plt.plot(broj_podjela,iznosi_analiticki, c='g', label='analiticki')
plt.xlabel('broj podjela')
plt.ylabel('iznos integracije')
plt.legend(loc='upper right')
plt.title("Integracija funkcije funkcije x^2 - 2*x")
plt.show()
