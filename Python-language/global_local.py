'''
# 作用域
globals()
locals()

LEGB
local -> enclosing function -> globals -> buitins

check all builtins
dir(__buitins__)

'''


n = 100
def space():
    n = 200
    def space2():
        n = 300
        print(n)
    return space2

n = space()
n()