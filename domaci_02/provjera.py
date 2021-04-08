import zadatak_1__nacin_1 as har
import zadatak_1__nacin_2 as zar
import math as m

p1 = har.Grafovi(0,2,0)
p1.plot(0.01,p1.gravitacijska_sila(-9.81))    #minus kako bi gibanje bilo u +y smjeru
p1.reset()

p1 = har.Grafovi(3,2,0)
p1.plot(0.01,p1.elasticna_sila(10))
p1.reset()

p1 = har.Grafovi(3,2,0)
p1.plot(0.001,p1.otpor_zraka(1,2,1),p1.elasticna_sila(10))   #prigušeno titranje
p1.reset()

p1 = har.Grafovi(0,2,0)
p1.plot(0.01,p1.gravitacijska_sila(-9.81),p1.otpor_zraka(0.1,0.5,1))
p1.reset()


#drugi modul
p1 = zar.Grafovi(0,10,0,10,0.1,0.5,1)
p1.crtanje(0.001,"m*g")
p1.reset()

p1 = zar.Grafovi(0,10,0,10,0.1,0.5,1)
p1.crtanje(0.001,"m*g","-Cx*S*((Rho*(v**2))/2)")
p1.reset()

p1 = zar.Grafovi(3,10,0,10,0.1,0.5,1)
p1.crtanje(0.001,"-k*x")
p1.reset()