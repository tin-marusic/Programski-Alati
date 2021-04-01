import zadatak_1 as har
import math as m
p1 = har.Grafovi(m.sqrt(10),1,0)
p1.plot(0.01,p1.elasticna_sila(10))
p1.reset()
p1 = har.Grafovi(m.sqrt(10),1,0)
p1.plot(0.01,p1.gravitacijska_sila(10))
p1.reset()
p1 = har.Grafovi(3,10,0)
p1.plot(0.001,p1.otpor_zraka(3,3,3),p1.gravitacijska_sila(10))

