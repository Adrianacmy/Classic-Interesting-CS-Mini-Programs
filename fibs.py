'''different ways to count fibs'''

def fibs(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibs(n - 1) + fibs(n - 2)

def fibs2(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current


print(fibs2(4))