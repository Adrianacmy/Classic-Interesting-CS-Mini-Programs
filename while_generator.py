'''
a infinitely generator with while
'''

def while_generator(n):
    i = 0
    while True:
        if i == len(n):
            i = 0

        yield n[i]
        i += 1

n = [1, 2, 3, 4, 5]
gen = while_generator(n)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
