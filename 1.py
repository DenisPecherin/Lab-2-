import time
import math

# Сравните время вычисления 35-го числа Фибоначчи при помощи формулы Бине,
# итерационной формулы, метода «разделяй и властвуй», метода нисходящего динамического программирования,
# метода восходящего динамического программирования.

# Формула Бине
start = time.time()
answer = (pow((1 + math.sqrt(5))/2, 35)-pow((1 - math.sqrt(5))/2, 35))/math.sqrt(5)
print("Формула Бине")
print(int(answer))
print(time.time() - start)

# Итерационая формула
start = time.time()
def f_iteration(n):
        a, b = 1, 1
        for i in range(3,n+1):
            if (i%2 == 0):
                a+=b
            else:
                b+=a
        if (a>b):
            return a
        else:
            return b
print("Итерационая формула")
print(f_iteration(35))
print(time.time() - start)

# Разделяй и властвуй
start = time.time()

f_rv = lambda n: f_rv(n - 1) + f_rv(n - 2) if n > 2 else 1

print("Разделяй и властвуй")
print(f_rv(35))
print(time.time() - start)

# Нисходящие ДП
start = time.time()

ndp = {0: 0, 1: 1}
def f_ndp(n):
    if n in ndp:
        return ndp[n]
    ndp[n] = f_ndp(n - 1) + f_ndp(n - 2)
    return ndp[n]

print("Нисходящие ДП")
print(f_ndp(35))
print(time.time() - start)

# Восходящие ДП
start = time.time()

def f_vdp(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

print("Восходящие ДП")
print(f_vdp(35))
print(time.time() - start)