# Harjutus 11

# def tervita(k):
#     print("Tere", k) #KOheselt määratletud, et väljastab väärtuse

# def tervita2():
#     return("Tere kosmos!") #Annab väärtuse, hilisemalt saab määrata tegevuse sellele 

# tervita("jobu")
# print(tervita2())


# Kirjuta funktsioon, mis kontrollib, kas kahest sõnast koosnev sõne algab sama tähega.
# print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
# print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False

def sarnased_esitahed(s):
    s1, s2 = s.split(" ")
    #print(s1[0], s2[0])
    if s1[0].capitalize()==s2[0].capitalize():
        return True
    else:
        return False
    

print(sarnased_esitahed('Vapper vares'))
print(sarnased_esitahed('Lahe Känguru'))