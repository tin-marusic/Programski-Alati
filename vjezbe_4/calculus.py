import math as m
import numpy as np
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
                break
        else:
            x = x - h
            if y > x:
                break

    return der,xtocke

def integral_pravokutnik(f,a,b,n):
    x = np.linspace(a,b,n+1)
    y = f(x)
    y_d = y[1:]
    y_l = y[:-1]
    dx = (b-a)/n
    gornja_meda = dx * np.sum (y_d)
    donja_meda = dx * np.sum (y_l)
    return gornja_meda , donja_meda


def integral_trapez(f,a,b,n):
    x = np.linspace(a,b,n+1)
    y = f(x)
    y_d = y[1:]
    y_l = y[:-1]
    dx = (b-a)/n
    iznos = (dx/2) * np.sum(y_d + y_l)
    return iznos

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

def integ_f1(x):
    return (x**3)/3 - x**2
