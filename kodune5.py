#5. Kaugushüpe
#	kasutaja sisestab 3 kaugushüppe tulemust - 1p
#	sinu programm leiab ning väljastab parima ja keskmise tulemuse - 2p
#	programmi dialoog kasutajaga on arusaadav ja üheselt mõistetav - 1p
#	kood kommenteeritud - 1p

print("Kaugushüpe")#Pealkiri
print("")

katse1 = float(input("Sisesta esimese hüppe tulemus: "))#Esimese katse tulemuse sisend
katse2 = float(input("Sisesta teise katse tulemus: "))#Teise katse tulemuse sisend
katse3 = float(input("Sisesta kolmanda katse tulemus: "))#Kolmanda katse tulemuse sisend

list = [katse1, katse2, katse3]#Nimekirja koostamine
print("Katsete tulemused on: ",list)#Katse tulemuse sisestuse kuvamine
print("Sinu kõige pikem hüpe oli: ",max(list))#Pikima hyppe väljund
keskmine = sum(list) / len(list)#Keskmise hyppe väärtuse arvutusvalem
print("Sinu keskmine tulemus on: ",keskmine)#Keskmise hüppe väljund

