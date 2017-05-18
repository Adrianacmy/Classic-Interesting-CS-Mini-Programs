Python 3.6
1	import turtle
2	
3	def tree(branchLen,t):
4	    if branchLen > 5:
5	        t.forward(branchLen)
6	        t.right(20)
7	        tree(branchLen-15,t)
8	        t.left(40)
9	        tree(branchLen-15,t)
10	        t.right(20)
11	        t.backward(branchLen)
12	
1
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()
