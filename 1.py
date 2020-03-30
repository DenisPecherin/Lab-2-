import timeit

# Сравните время вычисления 35-го числа Фибоначчи при помощи формулы Бине,
# итерационной формулы, метода «разделяй и властвуй», метода нисходящего динамического программирования,
# метода восходящего динамического программирования.

# Формула Бине
code_to_test1 = """
from pervoe_zadanie1 import f1
"""
print("Формула Бине")
elapsed_time1 = timeit.timeit(code_to_test1, number=100)/100
print(elapsed_time1)


# Итерационая формула
code_to_test2 = """
n = 35
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
"""
print("Итерационая формула")
elapsed_time2 = timeit.timeit(code_to_test2, number=100)/100
print(elapsed_time2)


# Разделяй и властвуй
code_to_test3 = """
n = 35
f_rv = lambda n: f_rv(n - 1) + f_rv(n - 2) if n > 2 else 1
"""
print("Разделяй и властвуй")
elapsed_time3 = timeit.timeit(code_to_test3, number=100)/100
print(elapsed_time3)


# Нисходящие ДП
code_to_test4 = """
n = 35
ndp = {0: 0, 1: 1}
def f_ndp(n):
    if n in ndp:
        return ndp[n]
    ndp[n] = f_ndp(n - 1) + f_ndp(n - 2)
    return ndp[n]
"""
print("Нисходящие ДП")
elapsed_time4 = timeit.timeit(code_to_test4, number=100)/100
print(elapsed_time4)


# Восходящие ДП
code_to_test5 = """
n = 35
def f_vdp(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a
"""
print("Восходящие ДП")
elapsed_time5 = timeit.timeit(code_to_test5, number=100)/100
print(elapsed_time5)
