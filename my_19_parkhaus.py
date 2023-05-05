#parkhaus
# Freier Parkplatz → None
#Belegter Parkplatz → str
#z.b. VW Gold oder "Opel Astra"

parkhaus = [
    ["VW Käfer", "Porsche Boxter", "Opel Astra", "Trabant 601"],
    ["Toyota MR2", 'Mi 42', 'Fiat Punto', "VW GOLF"],
    ["VW T3", 'F4E Phantom 2', 'Citroën 2CV', None]
]

'''
Entwickle ein Parkhaus-System

In diesem Programm hat der Nutzer folgende Möglichkeiten:
1) Sein Auto in einer bestimmten Ebene parken
    -dazu muss der Nutzer eine Ebene eingeben
    -anschließend wird ihm der erste freie Platz zugewiesen
    -fals die Ebene voll ist, weise den Nutzer darauf hin
2) Sein Auto in dem ersten freien Parkplatz des ganzen(!) Parkhauses zu Parken
    - ablauf: schleife, welche die Ebenen durchläuft
        und eine, welche die plätze der aktuellen Ebene prüft
Hinweis:
- teste dein Programm mit unterschiedlichen Parkhaus-konfigurationen
    1) Ebene 1 voll, nutzer will in Ebene 1 parken
    2) alle Ebenen voll, nutzer will in Ebene 1 parken
    3 alle Ebenen voll, nutzer wählt menupunkt 2), nächster parkplatz
    4) alle plätze voll bis auf Ebene 3 letzter platz, nutzer wählt menupunkt 2)
'''

while True:
    auto_oder_manuell = input('1) Auto in einer bestimmten Ebene parken \n2) Auto in dem ersten freien Parkplatz zu Parken \n>>>')
    if auto_oder_manuell == '1' or auto_oder_manuell == str.lower('eins'):
        frage_etage = input ('Bitte Ebene wählen 1 - '+ str(len(parkhaus)) + '\n>>>')
        while True:
            if frage_etage.isdigit() and int(frage_etage) <= len(parkhaus):
                etage = int(frage_etage) - 1
                break
            elif frage_etage == str.lower('q'):
                quit()
            else:
                print('Falsche Eingabe')
                continue

        if None in parkhaus[etage]:
            print('Ihr platz befindet sich auf Ebene ' + frage_etage + ' Platz ' + str(parkhaus[etage].index(None) + 1))
            quit()
        else:
            print('Kein Parkplatz in Ebene '+ frage_etage +  ' mehr frei')

    elif auto_oder_manuell == '2' or auto_oder_manuell == str.lower('zwei'):
        for etage in parkhaus:
            for parkplatz in etage:
                if parkplatz == None:
                    print ('Ihr Parkplatz befindet sich auf Ebene '+ str(parkhaus.index(etage) + 1) + ' Platz ' + str(parkhaus[parkhaus.index(etage)].index(parkplatz) + 1))
                    quit()
                
        print ('Kein Parkplatz Frei')
        quit()
                    
    elif auto_oder_manuell == 'q':
        quit()
    else:
        print('Falsche eingabe')
