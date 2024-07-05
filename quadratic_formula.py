# TODO
x1 = ...
x2 = ...

print(x1, x2)




def math(a,b,c):
 xa = (-b + (b**2-4*a*c)**(1/2))/(2*a)
 xb = (-b - (b**2-4*a*c)**(1/2))/(2*a)
 Ans = f"{a}x^2+{b}x+{c}=0"
 if xa == xb:
    return (Ans,"Answer",xa)
 else:
    return (Ans,"Answer",xa,xb)


print(math(1,-6,9))
print(math(1,2,-8))
print(math(8,-6,-35))
print(math(1,0,1))    #?
