"""
Erstelle ein Bank-Programm

Ersteinmal loggt der Nutzer sich ein.
Sollte der Login erfolgreich sein 
(=name & pin korrekt),
kann er auf das Programm zugreifen.

Der Nutzer hat folgende Optionen:
1) Kontostand anzeigen (in x.xx €)
2) Kontostand erhöhen
3) Kontostand verringern
   - beachte: man kann nicht mehr abheben als auf dem Konto ist

BONUS)
Entwickle ein User-Management-Menü. Hier kann ein Admin folgendes:
1) Nutzer hinzufügen
2) Nutzer entfernen
"""
import os

user_db = [
    {
        "name": "admin",
        "pin":"admin",
        "balance":None
    },
    {
        "name": "Esad",
        "pin": "1234",
        "balance": 0
    },
    {
        "name": "Rafael",
        "pin": "9876",
        "balance": 100
    }
]

# TODO: Login-System implementieren

def login():
    name = input("Bitte Name eingeben: ")
    if name == "x":
        exit()

    for elem in user_db:
        if name in elem.values():
            counter = 0
            while True:
                counter += 1
                if counter == 4:
                    print("Zu viele Fehlversuche, konto wurde gesperrt")
                    exit()

                elif input("Bitte Pin für "+ user_db[user_db.index(elem)]["name"] + " eingeben: ") == user_db[user_db.index(elem)]["pin"]:
                    print("Wilkommen "+ user_db[user_db.index(elem)]["name"])
                    os.system("pause")
                    break

                else:
                    print("Falsche PIN Versuche übrig ", 3
                    - counter )

            return user_db.index(elem)
    
    print("Nutzer "+ name + " nicht gefunden")
    os.system("pause")
    os.system("cls")
    login()

def main():
    user_id = login()

    if user_db[user_id]["name"] == "admin":
        admin_mode()
    else:
        user_mode(user_id)

def admin_mode():
    while True:
        os.system("cls")
        print("### Bank-System ### Admin-Mode")
        print("Du hast folgende Optionen:")
        print("[1] Konto anlegen")
        print("[2] Konto entfernen")
        print("[x] Admin Mode beenden")
        eingabe = input(">>> ")
        
        if eingabe == "x":
            main()

        if eingabe == "1":
            neuer_name= input("Bitte Namen für Neukunden eingeben: ")
            while True:
                neuer_pin = input("Bitte Pin eingeben: ")
                if neuer_pin.isdigit() and len(neuer_pin) == 4:
                    user_db.append(
                        {
                            "name":neuer_name, 
                            "pin":neuer_pin, 
                            "balance":0
                        }
                    )
                    break
                else:
                    print("pin muss eine 4stellige zahl sein")
            os.system("pause")

        elif eingabe == "2":
            for i in range(len(user_db) - 1):
                print(i + 1, ".",  user_db[i+1]["name"])
            who_delete = input("Bitte Kundeneintrag zum löschen angeben: ")
            if who_delete.lower() == "x":
                exit()
            elif who_delete.isdigit() and 0 < int(who_delete) < len(user_db):
                del user_db[int(who_delete)]
                print("Nutzer gelöscht")
                os.system("pause")
            else:
                print("Das habe ich nicht verstanden!")
                os.system("pause")

        else:
            print("Das habe ich nicht verstanden!")
            os.system("pause")


def user_mode(user_id):
    while True:
        os.system("cls")
        print("### Bank-System ### Kunde: "+ user_db[user_id]["name"])
        print("Du hast folgende Optionen:")
        print("[1] Kontostand anzeigen")
        print("[2] Kontostand erhöhen")
        print("[3] Kontostand verringern")
        print("[x] Programm beenden")
        eingabe = input(">>> ")
        
        if eingabe == "1":
            print(f"Ihr Konstostand beträgt: " + "{:.2f} €".format(user_db[user_id]["balance"]))
            os.system("pause")
            
        elif eingabe == "2":
            v_balance_change = input("Wieviel möchten Sie einzahlen?: ")
            if v_balance_change.isdigit():
                user_db[user_id]["balance"] += int(v_balance_change)
                print("Einzahlung erfolgreich")
                os.system("pause")
            else:
                print("Das habe ich nicht verstanden!")
                os.system("pause")
            
        elif eingabe == "3":
            v_balance_change = input("Wieviel möchten Sie abheben?: ")
            if v_balance_change.isdigit():
                if user_db[user_id]["balance"] >= int(v_balance_change):
                    user_db[user_id]["balance"] -= int(v_balance_change)
                    print("Abhebung erfolgreich")
                    os.system("pause")
                else:
                    print("Der Betrag ist nicht gedeckt")
                    os.system("pause")
            else:
                print("Das habe ich nicht verstanden!")
                os.system("pause")

            
        elif eingabe == "x":
            exit()
            
        else:
            print("Das habe ich nicht verstanden!")
            os.system("pause")


main()