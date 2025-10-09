import turtle

#kolmnurg koodilõik
turtle.penup() #tõstab pliiatsi üles
turtle.goto(-400,200) #alguspunkti kordinaadid
turtle.pendown()
for i in range(3):
    turtle.fd(200)
    turtle.lt(120)

#see koodirida aitab korrata koodi
turtle.penup() #tõstab pliiatsi üles
turtle.goto(0,0) #alguspunkti kordinaadid
turtle.pendown()
for i in range(4):
    turtle.fd(150) #fd lühend
    turtle.lt(90) #lt lühend

#oma nimetähe kood
turtle.penup()
turtle.goto(200,200)
turtle.pendown()
turtle.fd(50)
turtle.lt(90)
turtle.fd(150)
turtle.lt(90)
turtle.fd(50)
turtle.lt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(50)
turtle.lt(90)
turtle.fd(50)
turtle.lt(90)
turtle.fd(150)
turtle.lt(90)
turtle.fd(50)
turtle.lt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(50)




               
               
               
turtle.done()