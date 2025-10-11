# Harjutus7

# nimede_loend = ["Mart", "Liis", "Jaan", "Kati", "Anu", "Marko"]
# 
# nimede_loend.append("Jyri")
# nimede_loend.insert(0,"Mari")
# for i in nimede_loend:
#     print(i)
# 
# Loo lugudest loend (koos numbrite ja jutumärkidega)
# 1. ALIKA – “Bridges”
# 2. Anett x Fredi – “Read Between The Lines”
# 3. villemdrillem – “leekiv armastus”
# 4. Clicherik & Mäx – “PAKSUD”
# 5. nublu – “ära ärata”
# 6. NOËP – “Move Your Feet”
# 7. Trad.Attack! – “Bring It On”
# 8. Bedwetters – “It Is What It Is”
# 9. Reket – “Panama paberid”
# 10. Grete Paia – “Võluväel”
# Kuva kasutajale kõik lood massiivist
# Küsi millist lugu ta “kuulata” soovib
# Kuva kasutaja valitud lugu

albumid = ['1. ALIKA – "Bridges"','2. Anett x Fredi – "Read Between The Lines"','3. villemdrillem – "leekiv armastus"','4. Clicherik & Mäx – "PAKSUD"','5. nublu – "ära ärata"','6. NOËP – "Move Your Feet"','7. Trad.Attack! – "Bring It On"','8. Bedwetters – "It Is What It Is"','9. Reket – "Panama paberid"','10. Grete Paia – "Võluväel"']

print (20*"-", "kõik lood",20*"-")

for i in albumid:
    print(i)
     
lugu = int(input("Millist lugu mängin: "))
print (f"Mängin: {albumid[lugu-1]}")



# Kasuta etteantud loendit ja toesta nõutud operatsioonid. Lisa igale tegevusele kommentaar ja vasta täislausega:
# “jaanuar”,-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3
# Kuva mõõdetava kuu nimetus
# Kuva viimase mõõtmise tulemus
# Kuva ainult temperatuurid
# Leia kuu maksimaalne ja minimaalne temperatuur
# Leia kuu keskmine temperatuur
# Mitu korda esines -20 kraadi
# Eemalda element nr 5
# Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
# Sorteeri temperatuurid nimekirjas kasvavas järjekorras

mootmised = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]

print(f"Mõõdetav kuu: {mootmised [0]}")
print(f"viimane mõõtmine: {mootmised [-1]}")
print(f"Mõõtmised :{mootmised[1:]}")
mootmised.pop(0)
print(f"min: {min(mootmised)} max:{(mootmised)}")
print(f"Keskmine temp: {round(sum(mootmised)/len(mootmised),2)}")
print(f"-20 kraadi esineb {mootmised.count(-20)} korda")
mootmised.pop(4)
mootmised.insert(4,44)
mootmised.sort()
print(mootmised)

