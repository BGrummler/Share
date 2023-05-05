""" ZAHLEN-RATE-SPIEL

a) Schreibe ein Programm, welches den Nutzer die geheime
   Zahl des Computers (Ganzzahl zwischen 1 und 10) erraten lässt.
   - Der Nutzer hat bis zu 2 Versuche
   - Sollte er es im ersten Versuch schaffen, kommt es
     nicht zu einem zweiten Versuch
   - Sollte er es im ersten Versuch nicht schaffen, hat
     er im zweiten eine weitere Chance

bonus) Gebe dem Nutzer Tipps, ob er zu hoch oder zu 
       niedrig geraten hat.
"""
# Zufallsnummer zwischen 1 und 10 generieren
spiel_gewonnen = 0
x = 123456789
y = 987654321
x = x + id(x) 
y = y + id(y)
global zufall
zufall = x + y
del x
del y
zufall=(zufall%10)+1



# EINGABE

schwierigkeit = input("\nPress [e] for easymode: ")
if schwierigkeit == str.lower("e"):
    print("\nEasymode activated")
elif schwierigkeit == str.lower("iddqd"):
    print ("\nCheatmode activated")
else:
    print("\nHardmode activated")


def eingabe():
    global nutzereingabe
    nutzereingabe = int(input("\nGib eine zahl swischen 1 und 10 ein: "))
    #print(nutzereingabe)
    if nutzereingabe > 0 and nutzereingabe < 10:
        print("\nMal sehen ob", nutzereingabe, "stimmt")
    else:
        print("falsche Eingabe\n")
        eingabe()

# VERARBEITUNG

versuche=0
def hardmode():
    eingabe()
    if nutzereingabe == zufall:
        global versuche
        global spiel_gewonnen
        spiel_gewonnen = 1
        versuche += 3
        #print("Hardmode gewonnen")
    elif versuche < 2:
        print(nutzereingabe," stimmt nicht, versuchs nochmal!")
    else:
        print("\n")

def easymode():
    eingabe()
    if nutzereingabe == zufall:
        global versuche
        global spiel_gewonnen
        spiel_gewonnen = 1
        versuche += 3
        #print("Easymode gewonnen")
    elif versuche < 2:
        if nutzereingabe > zufall:
            print(nutzereingabe, "ist höher als die gesuchte Zahl, versuchs nochmal !")
        else:
            print(nutzereingabe, "ist niedriger als die gesuchte Zahl, versuchs nochmal! ")
    else:
        print("\n")

def program_zahlenraten():
    global versuche
    global spiel_gewonnen
    versuche += 1
    if spiel_gewonnen == 1:
        print(nutzereingabe," stimmt  gratuliere !")
    
    elif versuche >= 3:
        print (nutzereingabe, "stimmt nicht, der Computer hatte",zufall, "Spiel Verloren\n")
    else:
            if schwierigkeit == str.lower("E"):
                easymode()
                program_zahlenraten()
            elif schwierigkeit == str.lower("iddqd"):
                print ("\n Der Computer wählt: ",zufall)
                easymode()
                program_zahlenraten()
            else:
                hardmode()
                program_zahlenraten()

program_zahlenraten()




# AUSGABE