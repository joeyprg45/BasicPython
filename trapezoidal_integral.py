from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------


#制御構文の課題
from math import pi

a =  pi / 2
b = 0
N = 100
h = (b-a)/N
S = 0
for k in range(1,N+1):
   S += (h/2)*(sin(a+(k-1)*h)+sin(a+k*h))

print(abs(S))


