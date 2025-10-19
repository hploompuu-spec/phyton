#4. Emaili kontroll
#	kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
#	programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll - 1p
#	programm tükeldab selle ja väljastab lause: ‘Tere enimi, sinu email on server serveris ja domeeniks on sul com’ - 1p
#	kasutajalt küsitud küsimused on selgelt üheselt mõistetavad - 1p
#	kood kommenteeritud - 1p

import re

print("E-posti kontroll")
print("")

def split_email(email):
    try:
        nime_osa, serveri_osa = email.split("@")
        nime_osad = nime_osa.split(".")
        serveri_osad = serveri_osa.split(".")

        enimi = nime_osad[0]
        pnimi = nime_osad[1] if len(nime_osad) > 1 else "(tundmatu)"
        server = serveri_osad[0] if len(serveri_osad) > 0 else "(tundmatu)"
        laiend = ".".join(serveri_osad[1:]) if len(serveri_osad) > 1 else "(tundmatu)"

        return enimi, pnimi, server, laiend
    except ValueError:
        return

email = input("Sisesta siia oma e-posti aadress: ")
enimi, pnimi, server, laiend = split_email(email)

def validate(email):
    pattern = r"^[a-zA-Z\d-]+\.[a-zA-Z\d-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        print("Tere", enimi, "sinu email on", server, "serveris ja domeeniks on sul", laiend)
    else:
        print("E-post aadress ei ole kehtiv")

validate(email)