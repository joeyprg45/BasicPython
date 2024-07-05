# TODO

c = 2
while True:
    print(1/c)
    c *= 100
    if  1 + 1/c == 1:
     break 


epsilon = 1.0
while (1.0 + epsilon) != 1.0:
    epsilon /= 2.0

epsilon *= 2.0
print(epsilon)