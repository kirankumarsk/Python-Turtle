import turtle
t =turtle.Turtle()
colors = ["blue", "green", "purple", "cyan", "magenta", "violet"]

t.reset()
for i in range(45):
     t.color(colors[i % 6])
     t.pendown()
     t.fd(2 + i * 5)
     t.left(45)
     t.width(i)
     t.penup()

