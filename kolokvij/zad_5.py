import kolokvij as kol
import matplotlib.pyplot as plt

p1 = kol.Vertikalni_Hitac(10,10)
visina_otpor , trajanje_otpor = p1.otpor(0.01,1,1)
p1.reset()

p1 = kol.Vertikalni_Hitac(10,10)
vrijeme = p1.trajanje(0.01)
visina = p1.max_visina(0.01)
p1.reset()

print(f"Maksimalna visina bez otpora je {visina},a sa otporom {visina_otpor}")
print(f"Maksimalno trajanje bez otpora je {vrijeme},a sa otporom {trajanje_otpor}")
