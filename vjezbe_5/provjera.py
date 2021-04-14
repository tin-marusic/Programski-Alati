import harmonic_oscillator as har
import math as m
p1 = har.HarmonicOscillator(m.sqrt(10),1,10,0)
p1.plot(0.01)
p1.reset()

p1 = har.HarmonicOscillator(m.sqrt(10),1,10,0)
p1.analiticko_rjesenje(0.001)
p1.reset()

p1 = har.HarmonicOscillator(m.sqrt(10),1,10,0)
p1.graf_prikaz()
p1.reset()