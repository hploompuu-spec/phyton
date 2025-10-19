#6. Salakeel
#	sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida - 1p
#	kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks - 1p
#	kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks - 1p
#	kood kommenteeritud - 1p

print("Salakeel")
print("")

def saladus_encode(message, shift=1):
    encoded = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encoded += chr((ord(char) - base + shift) % 26 + base)
        else:
            encoded += char
    return encoded

def saladus_decode(encoded, shift=2):
    return saladus_encode(encoded, -shift)

tegevus = input("Kas soovid salakeelt luua (sisesta: l) või tõlkida(sisesta: t): ")
teade = input("Sisesta lause: ")
encoded_teade = saladus_encode(teade)
decoded_teade = saladus_decode(encoded_teade)
if tegevus == "l":
    print("Loodud:", encoded_teade)

elif tegevus == "t":
    print("Tõlgitud:", decoded_teade)

else:
    print("Sisestasid oma soovi valesti!")

