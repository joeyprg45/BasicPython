#a = input("aの値を入力: ")
#b = input("bの値を入力: ")

# TODO


def sosuu(n):
 if type(n) == float:
   return "error"
 elif n <= 1:
   return "error"
 elif n > 1:
   for i in range(2, n):
        if n % i == 0:
         return "False"
        return "True"
 
print(sosuu(61)) #課題
print(sosuu(10)) #課題
print(sosuu(1))
print(sosuu(-5))
print(sosuu(3.14))
print(sosuu(37))

print(type(sosuu(61)))










