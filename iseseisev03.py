import turtle
import random

def joonista_ruut():
    for i in range(4):
        turtle.fd(100)
        turtle.lt(90)

def joonista_ring():
    turtle.circle(100)

def joonista_viisnurk():
    for i in range(5):
        turtle.fd(100)
        turtle.rt(144) 

def joonista_suvaline():
    kujund = random.choice(["ring", "ruut", "viisnurk"])
    if kujund == "ring":
        joonista_ring()
    elif kujund == "ruut":
        joonista_ruut()
    elif kujund == "viisnurk":
        joonista_viisnurk()

while True:
    kujund = input("Millist kujundit (ruut, ring, viisnurk, suvaline) sooviksid joonistada? ").lower()
    arv = input("Kui mitu kujundit sooviksite joonistada? ")

    try:
        arv = int(arv)
    except:
        print("Sisesta õige arv!")
        continue

    turtle.clear()

    for i in range(arv): 
        if kujund == "ruut":
            joonista_ruut()
        elif kujund == "ring":
            joonista_ring()
        elif kujund == "viisnurk":
            joonista_viisnurk()
        elif kujund == "suvaline":
            joonista_suvaline()
        else:
            print("Sellist kujundit polnud valikus!")
            break

        turtle.penup()
        turtle.fd(125)
        turtle.pendown()

    uuesti = input("Kas soovid korrata (jah/ei)? ").lower()
    if uuesti.lower() != "jah":
        print("Nägemist!")
        break

turtle.done()
