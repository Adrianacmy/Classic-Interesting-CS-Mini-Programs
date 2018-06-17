'''
return the greatest common divisor
'''

def gcd(m, n):
    if m > n:
        m, n = n, m
    for i in range(m, 0, -1):
        if m % i == 0 and n % i == 0:
            return i

print(gcd(12, 16))
