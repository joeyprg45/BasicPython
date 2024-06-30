#a = input("a の値を入力: ")
#b = input("b の値を入力: ")

# TODO

#---------------------------
a = 629     #試作
b = 259
while True:
    r = a%b
    a = b
    b = r
    print(b)

    if r == 0:
         break

#------------------------------------------
def euclid(a, b):    #本番（課題用）
    while not b == 0:
        if a < b:
         a,b = b,a

    a, b = b, a % b
    return a
    


result = euclid(20, 10)
result1 = euclid(14,91)
result2 = euclid(91,14)
print(result)
print(result1)
print(result2)




#------------------------------------------------------------------





     
