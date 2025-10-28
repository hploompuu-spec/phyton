# Proovin lahendada 14

import turtle

for i in range (9):
    turtle.penup()
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turtle.pendown()
    for i in range (4):
        turtle.lt(90)
        turtle.fd(100)
    turtle.penup()
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(10)

turtle.done()