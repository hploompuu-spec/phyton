#3. Täringud
#	kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
#	kasutaja võistleb kahe täringuga arvuti vastu - 1p
#	kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
#	kood kommenteeritud - 1p
from random import randint
print("Täringumäng")
print("")

number1 = randint(1, 6)  # Valib numbri vahemikust 1 kuni kuus ning salvestab selle number1 alla
number2 = randint(1, 6)  # Valib numbri vahemikust 1 kuni kuus ning salvestab selle number2 alla
number3 = randint(1, 6)  # Valib numbri vahemikust 1 kuni kuus ning salvestab selle number3 alla
number4 = randint(1, 6)  # Valib numbri vahemikust 1 kuni kuus ning salvestab selle number4 alla

summa1 = number1 + number2 #Arvutab mängija täringute summa
summa2 = number3 + number4 #Arvutab arvuti täringute summa

print("Veame kihla, kumma täringute summa on suurem?") #Küsimus
print("Sinu esimese täringu summa on ",number1," ja teise täringu summa on ",number2) #Andmed otsuse tegemiseks
panus = int(input("Kui suure summa peale kihla veame, et sinu täringute summa on suurem? ")) #Küsib panust

if summa1 < summa2:
    print("Ha ha! Vale!",panus," Eurot on minu! Mina viskasin",number3," ja ",number4,)#Tegevus, kui arvuti summa on suurem
    
else:
    print("Pagan! Sina võitsid! Mina viskasin",number3," ja ",number4,". Said ",panus," Eurot endale.")#Tegevus, kui mängija summa on suurem