import zadatak_1 as har
import math as m
#p1 = har.Grafovi(3,10,0,10)
#p1.plot(0.01,p1.elasticna_sila(10))
#p1.reset()

#p1.reset()
p1 = har.Grafovi(3,10,0,10)
p1.plot(0.01,p1.gravitacijska_sila(10))
p1.reset()
#p1 = har.Grafovi(3,10,0,10)
#p1.plot(0.001,p1.otpor_zraka(0.1,0.5,1),p1.gravitacijska_sila(10))
#p1.crtanje(0.001,"-k*x")
#p1.reset()

p1 = har.Grafovi(3,10,0,10)
p1.crtanje(0.001,"m*g")
p1.reset()