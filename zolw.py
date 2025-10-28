import time
import turtle


s = turtle.getscreen()
t = turtle.Turtle()


t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

t.circle(100)
t.rt(90)
t.fd(100)
t.circle(250)
t.fillcolor("red")
t.dot(20)
t.home()
turtle.bgcolor("blue")
turtle.bgcolor("light green")
time.sleep(1)
turtle.bgcolor("yellow")
time.sleep(1)
turtle.bgcolor("red")
time.sleep(1)
turtle.bgcolor("white")
time.sleep(1)
turtle.bgcolor("purple")
time.sleep(1)
turtle.bgcolor("blue")

turtle.mainloop()
