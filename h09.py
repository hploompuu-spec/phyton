# Harjutus 09

#13. Mitmemõõtmelise massiivi kasutamine for-tsükliga
#Tutvu elektriautode nimekirjaga, mis sisaldab 10 elektriauto mudelit, nende läbisõidu ulatust ja hinda. Mõista, kuidas andmed on struktureeritud.


ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]
lugeja = 0
r_kokku = 0
p_kokku = 0

for i in ev_data:
    print(f"{i[0]:30} {i[1]:10} {i[2]:40}") #vormindan andmed tulpadena, (:30, :10,:40) on laiused
    if (i[1]).isnumeric()==True:
        r_kokku+=int(i[1])
        p_kokku+=int(i[2])
        lugeja+=1 #lugeja 0 lugeja + 1

print(f"Sõidu ulatus keskmine: {r_kokku/lugeja}")
print(f"Hind keskmine: {p_kokku/lugeja}")   

print("")        
print("Autod, mis sõidavad kaugemale kui 300km")
for j in ev_data:
    if (j[1]).isnumeric()==True:
        if int(j[1]) >= 300:
            print(j[0])


print("")

parim_hinnasuhe = 1000000
parim_auto = ""

for l in ev_data:
    if (l[1]).isnumeric()==True:
        km_tasu = float(l[2]) / float(l[1])
        if km_tasu<parim_hinnasuhe:
            parim_hinnasuhe = km_tasu
            parim_auto =l[0]


print(f"Parim elektriauto: {parim_auto}")

    

# Kuva arvud 1-42
# Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
# Arvud, mis jagunevad 5, lisa tekst TAK (näiteks 5 TAK)
# Kui jagunevad mõlemaga, siis lisa tekst TIKTAK (näiteks 15 TIKTAK)
for i in range (1,42):
    if i%15 == 0:
        print(i,"TIKTAK")
    elif i%3 == 0:
        print(i,"TIK")
    elif i%5  == 0:
        print(i,"TAK")

    else:
        print(i)

