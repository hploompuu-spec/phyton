  #Harjutus 08#

tooted={
'piim': {'kogus': 20, 'hind': 1.19},
'küpsised': {'kogus': 20, 'hind': 4.99},
'või': {'kogus': 20, 'hind': 2.29},
'juust': {'kogus': 15, 'hind': 1.9},
'leib': {'kogus': 15, 'hind': 2.59},
'jogurt': {'kogus': 18, 'hind': 3.65},
'õunad': {'kogus': 35, 'hind': 3.15},
'apelsinid': {'kogus': 40, 'hind': 0.99},
'banaanid': {'kogus': 23, 'hind': 1.29}
}





telefonid={
'Mari': '5957503',
'Toomas': '5719979',
'Kertu': '5201750',
'Siim': '5580027',
'Piret': '5960799',
'Jaan': '5160415',
'Lea': '5760164',
'Mart': '5337951',
'Anni': '5004818',
'Tõnu': '5721873',
'Kai': '5811884',
'Rasmus': '5859489',
'Eva': '5039393',
'Oskar': '5635812',
'Liina': '5696114',
'Peeter': '5560756',
'Sandra': '5257415',
'Heiki': '5207248',
'Kristi': '5703338',
'Urmas': '5400549'
}

#Otsin Rasmuse telefoninumbri
print(telefonid['Rasmus'])

#lisa ennast nimekirja
telefonid["Hannes"] = 1213456789

print(telefonid['Hannes'])

#Kustuta Kristi number'
#popitud_vaartus = sonastik.pop('vanus', 'Ei ole olemas')

eemalda =telefonid.pop("Kristi")

print(telefonid)

#Muuda Eva telefoninumbri väärtuseks 55555555

telefonid['Eva'] = 55555555

# Kuva kõik numbrid

for i in telefonid:
    print(telefonid[i])

#Lisa võimalus kasutajal otsida nime järgi telefoninumbreid. Lisa teade, kui otsitavat nime ei leitud.

nimi = input("Lisa otsitava nimi: ").capitalize()
try:
    print(telefonid[nimi])
except:
    print("Sellist nime pole!!")

#2. Loo Pythoni programm, mis töötab etteantud mitmemõõtmelise sõnastikuga, järgides alltoodud juhiseid: 

print(tooted)
print(tooted["piim"]["kogus"])

# Programm peaks kasutajalt küsima toote nime, mida ta soovib osta
try:
    toode = input("Millist toodet soovid osta: ").lower()
    kogus = int(input("Kui palju sa seda soovid: "))

# Kui toodet ei ole, kuvatakse sõnum, et toodet ei leitud
    if toode in tooted.keys():
       if kogus <= tooted[toode]["kogus"]:
           print("-----Arve-----")
           summa = kogus * tooted[toode]["hind"]
           print(f"{summa} Eurot")
           tooted[toode]["kogus"] -= kogus #võtab maha
#        else:
           print("Pole piisavalt!")
    else:
        print(f"Toodet '{toode}' ei leitud!")


except:
    print("Ole normaalne!!")

tooted[toode]["kogus"] -= kogus #võtab maha


