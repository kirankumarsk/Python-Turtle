import turtle
turtle = turtle.Turtle()
turtle.left(20)
X=0
for i in range(0,60):
    turtle.left(X)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    X=X+10
