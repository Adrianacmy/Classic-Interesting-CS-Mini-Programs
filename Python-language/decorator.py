from collections import Iterable

# how decorator works and when it get called: https://www.youtube.com/watch?v=q2gi86yRVd0&index=14&list=PLe_BlddcFvNSSh1alKJemx0sfe1tF8Ldj


def test():
    print('test....')


def test():
    print('test2....')

#　重名函數不會報錯，　加載到第二個test, 第一個test應用會換指向第二個test函數體，　避免重名


'''
decorator: 不改變原函數的功能的前提下，　擴展原函數
'''


def verify(func):
    def wrapper():
        if isinstance([], Iterable):
            print('decorator1.....')
            func()
        else:
            print('redirect to login 1')
    return wrapper


def verify2(func):
    def wrapper():
        if isinstance([], Iterable):
            print('decorator2.....')
            func()
        else:
            print('redirect to login 2')
    return wrapper


# verify = verify(test)
# verify()
'''
verifing
test2....
'''


@verify
@verify2
def checkout():
    print('authenticated checkout')


# verify2 get called first
# below @verify is not a function, waiting for the resutl of @verify2
checkout()


# 通用裝飾器, 可裝飾Ｘ個參數，有返回值和無返回值的函數
def func(func_name):
    def func_in(*args, **kwargs):
        ret = func_name(*args, **kwargs)
        return ret
    return func_in




＃　帶有參數的裝飾器

def decorator_with_args(args):
    def func(func_name):
        def func_in():
            print('.....log.....{}'.format(args))
            ret = func_name()
            return ret
        return func_in
    return func


@decorator_with_args('something')
def test():
    print('....test....')

# 1.先執行decorator_with_args(args)函數，　這個函數return的結果就func這個函數的引用
# 2. ＠func
# 3. 使用@func 裝飾test

@decorator_with_args('anything')
def test():
    print('....test....')