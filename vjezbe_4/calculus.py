import math as m
def deriva3(f,a,h):
    return (f(a + h) - f(a - h))/(2*h)

def deriva2(f,a,h):
    derivate = (f(a+h)-f(a))/h
    return derivate


def der2(f,x,y,h,metoda = 3):
    xtocke = []
    der = []
    while True:
        if metoda == 2:
            a = deriva2(f,x,h)
        elif metoda == 3:
            a = deriva3(f,x,h)
        der.append(a)
        xtocke.append(x)
        if y>x:
            x = x + h
            if x > y:
               # x = x.round(x,0)
                break
        else:
            x = x - h
            if y > x:
                break

    return der,xtocke

def f1(x):
    return x*x-2*x

def f2(x):
    return 5*x**3 - 2*x**2 + 2*x -3
def f3(x):
    return 2*x**2-3

def f4(x):
    return m.sin(x)  
    
def deriv_f1(x):
    return 2*x - 2

def deriv_f2(x):
    return 15*x**2 - 4*x  + 2

def deriv_f3(x):
    return 4*x

def deriv_f4(x):
    return m.cos(x)

