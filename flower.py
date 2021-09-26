import turtle
t = turtle.Turtle()
t.reset()
t.color("red")
for angle in range(0, 360, 15):
 t.seth(angle)
 t.circle(100)

