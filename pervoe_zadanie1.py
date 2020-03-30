import math
def f1(n):
    answer = (pow((1 + math.sqrt(5))/2, n)-pow((1 - math.sqrt(5))/2, n))/math.sqrt(5)
    return answer
