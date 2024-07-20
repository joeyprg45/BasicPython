#a = input("aの値を入力: ")
#b = input("bの値を入力: ")

# TODO


def sosuu(n):
    if not isinstance(n, int):
        raise TypeError("int型以外の入力は受け付けません")
    elif n < 1:
        raise ValueError("入力は自然数である必要があります")
    elif n == 1:
        return False
    elif n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

print(sosuu(61))
print(sosuu(10))
print(sosuu(1))
print(sosuu(-5))
print(sosuu(3.14))
print(sosuu(13))


print(type(sosuu(61)))
