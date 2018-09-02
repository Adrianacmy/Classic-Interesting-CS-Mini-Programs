'''



'''
# () to create a generator
c = (x*2 for x in range(10))
# next(c)

#　沒有第三個變量的前提下交換二兩變量的值
a = 10
b = 9

a = a + b
b = a - b
a = a - b

# 結果
a = 9
b = 10


# create generator with yield
# fibonachi
# 到 yield , 停，　返回b 的值，　下一次從上次停下的點開始
def fibo():
    print('......fibo start......')
    a, b = 0, 1
    for i in range(5):
        print('....genertor 1....')
        yield b
        print('....genertor 2....')
        a, b = b, a+b
        print('....genertor 3....')
    print('.....generator stop.....')


a = fibo()
next(a)
a.__next__()
# above two ways are the same, will be stopIteration exception


# 這種方式調用避免exception
for i in a:
    print(i)


def generator_test():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1


t = generator_test()
t.__next__()
t.send('next temp')


# generator 應用： 多任務, 協程
def g1():
    while True:
        print('......g1...')
        yield None


def g2():
    while True:
        print('......g2...')
        yield None

t1 = g1()
t2 = g2()
while True:
    t1.__next__()
    t2.__next__()

