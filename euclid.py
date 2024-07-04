#a = input("a の値を入力: ")
#b = input("b の値を入力: ")

# TODO

#---------------------------


#------------------------------------------
def euclid(a, b):    #本番（課題用）
    while b != 0:
     a, b = b, a % b
    return a
    


result = euclid(20,10)
result1 = euclid(14,91)
result2 = euclid(91,14)

print(result)
print(result1)
print(result2)




#------------------------------------------------------------------





     
