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
    # Sisend väärtuse saamiseks kas EEK või EUR
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