# Python Libs Exploring

This repo contains all my experiment codes while playing with libs.

## Standard libs

- [Turtle graphics for Tk](./draw_mystery/) [Documentation](https://docs.python.org/3.6/library/turtle.html)
- [Smtplib to send emails](./send_email)   [Documentation](https://docs.python.org/3/library/smtplib.html)

## Third party packages

- [BeautifulSoup](./besoup/) [Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Numpy](./Numpy) [Documentation](https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html#reference)

- [Pandas](./Pandas) [Documentation](http://pandas.pydata.org/pandas-docs/stable/)


# Python Language

## sys
- If import xx can not find: `sys.path.append(xmodule)`
- After update a moudle while in ipython, `reload(xmoudle)` to reload updated feature


## == and is

- `a = ['a', 'b'], - b = ['a', 'b']`
- `a == b`: 值比較
- `a is b`: 是否指向同一個對象
- `a = 100, b = 100, a is b`

```python
if n >= -5 and n <= 127:
    a = n
    b = n
    a is b # True

if m >= -5:
    a, b = 789, 789
    a is b #True

    a, b = -6, -6
    a is b #False

```

## shallow copy vs deep copy
- [docs](https://docs.python.org/3.6/library/copy.html)
```
a = [11, 12]
b = a　＃shallow copy, reference copy

import copy
c = copy.deepcopy(a) # deep copy, value copy, recursive copy
c = copy.copy(a) # 如果a可遍歷，　拷一層，　如果不可遍歷，如tuple, 直接指向其地址


d = [1,2,3]
e = [4,5,6]
f = [d, e]
g = copy.deepycopy(f) # value copy
h = copy.copy(f) # reference copy
d.append(9)

f # [[1, 2, 3, 9], [4, 5, 6]]
g # [[1, 2, 3], [4, 5, 6]]
h # [[1, 2, 3, 9], [4, 5, 6]]


f = (d, e) #元組不可遍歷
g = copy.deepycopy(f) # value copy
h = copy.copy(f) # reference copy
d.append(9)

f is h # true

```

## 進制轉換
- positive number: 　原碼　＝　反碼　＝ 補碼
- negative number: 　
    - 反碼：　符號位不變，　其他位取反
    - 補碼：　反碼　＋　１

- +1原碼:  0000 0000 0000 0001
- -1原碼 : 1000 0000 0000 0001
- -1反碼 : 1111 1111 1111 1110
- -1補碼 : 1111 1111 1111 1111

- -1 + 1 : -1 的補碼　＋　１的補碼
```python

　 1111 1111 1111 1110  +
 　0000 0000 0000 0001
------------------------------
 　0000 0000 0000 0000

 1, int 只有兩個字節，　所以進的一位去掉

 a = 18
 bin(18) #0b10010
 oct(18) #0o22
 hex(18) #0x12

 int('0b10010', 2)
 int('0o22', 8)
 int('0x12', 16)

```

## 位運算
- a << 2: a*2*2
- a >> 1: a // 2
- &: 按位與: 有一個０則０
- |: 按位或, 有一個1則1
- ^: 異或，只要不同則爲1
- ~: 取反(補碼), ~12

```
~9
9

1000 1001  (9)
1111 0110  取飯
0000 0001   (＋1)

1000 1010

-10

```

## 私有化, [property](https://docs.python.org/2/library/functions.html#property)

- xx: public
- __xx: private property or method. Use setter and getter to make it callable to its instances
- __xx__:Python build-in
- _xx, xx_: avoid conflict with Python keywords,
```
modulex(object):
    number = 40
    _number = 20
    __number = 30

    def __init__(self):
        self.__num = 20

    def setNumber(self, newNumber, newApple):
        self.__number = newNumber
        self.__apple = newApple

    def getNumber(self):
        return self.__number

    num = property(getNumber, setNumber)

    @property
    def apple(self):
        return self.__apple

    @apple.setter
    def apple(self, newApple):
        self.__apple = newApple

    @apple.deleter
    def apple(self):
        del self.__apple
    # how to call deleter


from modulex import *
_number #not defined
__number #not defined

import modulex
modulex._number #20
modulex.__number #30

m = modulex()
m.__num # not defined, name mangling into _modulex__num
m._modulex__num # 20

m.num = 80 # m.setNumber(80)
m.num # 30 # m.getNumber()

m.apple = 100 # setter
m.apple # 100

```

## Iterator

- `isinstance((x for x in range(10)), Iterator)` # True
- `isinstance([], Iterator)` # False
- `isinstance([], Iterable)` # True
- convert list into iterator:
```
lst = [1,2,3,5]
isinstance(iter(lst), Iterator) # True

```

## Closure

## 多任務: 輪詢，優先度調用

- 併發：　任務多餘內核書
- 並行: 任務　<= 內核數
- 全局變量在多個進程中不共享

- 進程：　運行中的程序
```
ret = os.fork() #create a child process, 執行順序不確定
if ret > 0:
    print('fu')
else:
    print('zi')

os.getpid()
os.getppid() # parent process id


import os
os.fork()
os.fork()
os.fork()
# created 8 process in total after above three lines

# fork 炸彈
while True:
os.fork()

```