#Harjutus5
import random
import turtle
# Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
# Kirjuta programm, mis simuleerib mündiviskamist. Programm genereerib juhusliku tulemuse – “kiri” või “kull”, kasutades random.randint(0,1) funktsiooni. Programmi koostamisel pead importima import random mooduli ja kasutama randint() funktsiooni, et valida kahe võimaliku tulemuse vahel. Näiteks, kui randint(0, 1) annab tulemuseks 0, siis võib see tähendada “kirja”, ja 1 võib tähendada “kulli”.
# Seejärel palub programm kasutajal arvata, kumb külg maandub ülespoole.
# Kasuta if lauset, et kontrollida, kas kasutaja arvas õigesti. Kui arvas õigesti, siis joonista Turtle abil roheline ring; kui valesti, siis punane ring.

mynt = random.randint(0,1)
arvamus = input("kull või kiri: ")

if mynt == 1 and arvamus=="kiri":
    print("Tubli!")
    turtle.color("green")
    turtle.circle(50)
elif mynt == 0 and arvamus =="kull":
    print("Tubli!")
    turtle.color("green")
    turtle.circle(50)
else:
    print("Vale!")
    turtle.color("red")
    turtle.circle(50)


# Sama mis eelmine ainult arvuti valib ise numbri (vajalik eelnevalt sisse tuua random funktsioon: kirjuta algusesse import random)

arv1 = random.randint(1,10)
arv2 = random.randint(1,10)
tehe = arv1 * arv2
vastus = int(input(f"{arv1} x {arv2} = "))
if vastus == tehe:
    print("Õige vastus")
else:
    print("Loll oled vä?")

# Matemaatika test (randint)
# Kirjuta programm, mis kontrollib kasutaja poolt sisestatud vastust lihtsale matemaatikaülesandele.
# Näiteks, programm esitab küsimuse “Mis on 3 korda 4?”. Kasutaja peab sisestama vastuse. Kui kasutaja vastus on 12, siis programm väljastab “Õige vastus!”, kui aga vastus on midagi muud, siis väljastab “Vale vastus, proovi uuesti!”.
# Kasuta if ja else lauseid selleks, et kontrollida kasutaja sisestatud vastust.

arv1 = 3
arv2 = 4
tehe = arv1 * arv2
vastus = int(input(f"{arv1} x {arv2} = "))
if vastus == tehe:
    print("Õige vastus")
else:
    print("Loll oled vä?")

# Vanusepiiranguga üritus
# 		Sa oled loomas programmi, mis aitab kontrollida, kas inimesed vastavad vanusepiirangu nõuetele üritusel osalemiseks.
# 		Programm palub kasutajal sisestada oma vanuse. Kui vanus on vähemalt 18 aastat, siis programm annab teada, et kasutaja võib üritusele siseneda. Kui vanus on alla 18, siis programm teatab, et üritusele sisenemiseks ei ole piisavalt vana.
# 		Kasuta if ja else lauseid, et luua see vanusekontrolli programm.

vanus = int(input("Lisa vanus:"))
if vanus>=18:
    print("Võib siseneda!")
else:
    print("Marss koju tagasi!!")
    
turtle.done()