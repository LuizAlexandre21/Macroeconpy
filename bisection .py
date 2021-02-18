import numpy as np

def bisection(f,a,b):
  if f(a)*f(b)>0:
    print("Escolha errada para a e b")
  else:
    c=(a+b)/2
    err = np.abs(f(c))
    while err>1e-7:
        if f(a)*f(c)<0:
            b = c
        else:
            a = c
            c = (a+b)/2
            err = np.abs(f(c))



f = lambda x: x**2 - x - 1
approx_phi = bisection(f,1.2,2.5)
print(approx_phi)
