import turtle
tr = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-300, -300, 300, 300)

f = open('mystery.txt', 'r')
for aline in f:
    lst_line = aline.split()
    if lst_line[0] == 'UP':
        tr.up()
    elif lst_line[0] == 'DOWN':
        tr.down()
    else:
        tr.goto(int(lst_line[0]), int(lst_line[1]))

f.close()
wn.exitonclick()
