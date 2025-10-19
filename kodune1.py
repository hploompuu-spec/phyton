# Harjutus 1

#1. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
#	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
#	eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
#	kood mis teavitab paaris või paaritust arvust - 1p
#	kuvatakse programmi pealkiri - 1p
#	kood kommenteeritud - 1p

print("Arvude kontroll")#Pealkiri
print("")
try:
    arv = int(input("Tahad teada kas arv on paaris või paaritu? Sisesta siia arv:")) # Küsimus koos arvu salvestamisega
    if arv % 2 == 0: #Arvu kontroll koos vastusevariantidega
            print("Paaris")
    else:
            print("Paaritu")
except ValueError: #Tegevus kui arv ei vasta ette antud väärtusele
    print("Sisestasid arvu valesti!")
