import turtle
#Tervitus
nimi = "Juhan"
vanus = 58
keskmine_hinne = 4.7

print(nimi,",",vanus,"aastat vanaja keskmine hinne on",keskmine_hinne)

#Ostunimekiri
toode = "porgandeid"
kogus = 3
hind = 5.35

print("Soovin "+toode+" "+str(kogus)+", mille tüki hind on "+str(hind)+" eurot")

#Reisiplaan
sihtkoht = "Haapsalu"
paevade_arv = 5
oobimise_hind = 100

kokku = paevade_arv * oobimise_hind

print(sihtkoht,"reis kestab",paevade_arv,"päeva ja üks öö maksab",kokku,"eurot.")


#Python Turtle ruut
kylje_pikkus = 100
nurk = 90
kujundi_varv = "blue"
x = 110
kordaja = x * 1,5

turtle.pencolor(kujundi_varv)
for j in range(3):
    for i in range(4):
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()            
    turtle.goto(x,0)
    turtle.pendown()
    x = x * 2

turtle.done()