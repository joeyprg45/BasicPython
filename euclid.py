a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO


def euclid2(a, b):
    if a < b:
      a,b = b,a

    while not b == 0:
        a, b = b, a % b
    return a
    

def judge(a,b):
    return euclid2(a,b) == 1

result1 = euclid(12, 25)
result2 = judge(12, 25)
print("最大公約数" ,result1)
print("素数判定" ,result2)


#エクストラ問題
import random
import math

def are_coprime(a, b):
    return math.gcd(a, b) == 1

count = 0
total = 100000

for _ in range(total):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    if are_coprime(a, b):
        count += 1

probability = count / total
print(probability)
