from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

from math import pi
from math import exp

def integral(f,a=0,b=1,n=100):
   h = (b-a)/n
   S = 0
   for k in range(1,n+1):
    S += (h/2)*(f(a+(k-1)*h)+f(a+k*h))
   return(abs(S))

print(integral(lambda x: sin(x),0,pi/2,50))
print(integral(lambda x: 4 / (1 + x**2),0,1,100))
print(integral(lambda x: pi**(1/2)*exp(-x**2),-100,100,1000))
