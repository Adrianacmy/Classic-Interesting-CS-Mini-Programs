'''
closure:　在函數內部再定義一個函數，並且這個函數用到了外邊函數的變量
outer function return the reference of inner function
應用：　簡化函數調用，　不用總是提供所有參數
'''


def outer(a, b):
    print('.....1.....')
    def inner(x):
        print('....2.....')
        return a*x + b

    print('.......3.....')
    return inner

a = outer(4, 5) # call outer once, how to understand outer will always exist while inners exeu, innder is inside the outer stack ?

print(a(2))
print(a(5))

'''
.....1.....
.......3.....
....2.....
102

'''

