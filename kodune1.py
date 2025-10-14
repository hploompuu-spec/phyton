# Harjutus 1

#1. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
#	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
#	eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
#	kood mis teavitab paaris või paaritust arvust - 1p
#	kuvatakse programmi pealkiri - 1p
#	kood kommenteeritud - 1p

print("Arvude kontroll")
print("")
try:
    arv = int(input("Tahad teada kas arv on paaris või paaritu? Sisesta siia arv:")) # Küsimus koos arvu salvestamisega
    if arv % 2 == 0: #Arvu kontroll koos vastusevariantidega
            print("Paaris")
    else:
            print("Paaritu")
except ValueError: #Tegevus kui arv ei vasta ette antud väärtusele
    print("Sisestasid arvu valesti!")


# Harjutus 2

#2. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
#	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
#	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
#	küsitakse valuuta kogust ja tehakse arvutused - 2p
#	kood kommenteeritud - 1p

print("Eurokalkuraator")
print("")

try:
    valuuta = input("Euro väärtuse arvuramiseks kirjuta sõna EUR ja krooni väärtuse saamiseks sõna EEK:")
    # Sisend väärtuse saamiseks kas EEk või EUR
    vaartus = float(input("Sisesta summa:"))    # Sisend summa saamiseks

    if valuuta =="EUR": # Arvutab väärtuse EUR korral
        summa = float(vaartus / 15.6466)
        print(vaartus," krooni eest saab",summa,"Eurot.")

    elif valuuta =="EEK": # Arvutab väärtuse EEk korral
        summa = float(vaartus * 15.6466)
        print(vaartus," Euro eest saab",summa,"krooni.")

    else: # Annab veateate kui rahaühiku väärtus on valesti
        print("Sisestasid rahaühiku valesti!!")

except: # Annab veateate kui summa valesti
    print("Midagi valesti???")

#3. Täringud
#	kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
#	kasutaja võistleb kahe täringuga arvuti vastu - 1p
#	kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
#	kood kommenteeritud - 1p


#4. Emaili kontroll
#	kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
#	programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll - 1p
#	programm tükeldab selle ja väljastab lause: ‘Tere enimi, sinu email on server serveris ja domeeniks on sul com’ - 1p
#	kasutajalt küsitud küsimused on selgelt üheselt mõistetavad - 1p
#	kood kommenteeritud - 1p

#5. Kaugushüpe
#	kasutaja sisestab 3 kaugushüppe tulemust - 1p
#	sinu programm leiab ning väljastab parima ja keskmise tulemuse - 2p
#	programmi dialoog kasutajaga on arusaadav ja üheselt mõistetav - 1p
#	kood kommenteeritud - 1p

#6. Salakeel
#	sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida - 1p
#	kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks - 1p
#	kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks - 1p
#	kood kommenteeritud - 1p