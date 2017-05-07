'''
:return the lowest common mutiple

'''

def lcm(n1, n2):
    if n1 > n2:
        n, n2 = n2, n1

    for i in range(n2, n1 * n2 + 1, n2):
        if i % n1 == 0 and i % n2 == 0:
            return i


print(lcm(3, 5))
print(lcm(2, 4))
