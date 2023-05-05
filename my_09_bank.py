"""
Entwickle ein Bank-System

Der Nutzer hat einen Kontostand, welcher zu Beginn bei 100 liegt.
Im Hauptmenü wird dem Nutzer der aktuelle Kontostand angezeigt.

Über das Untermenü 1 kann der Nutzer den Kontostand erhöhen
- Der Geldbetrag MUSS eine Zahl sein
- Es muss eine Möglichkeit geben, in das Hauptmenü zurückzukehren

Über das Untermenü 2 kann der Nutzer den Kontostand verringern
- Der Geldbetrag MUSS eine Zahl sein
- Es muss eine Möglichkeit geben, in das Hauptmenü zurückzukehren

BONUS) Der Nutzer darf nicht mehr Geld abheben (Untermenü 2)
       als ihm zur Verfügung steht

BONUS_2) Implementiere eine PIN-Abfrage für das Konto
"""

import random
import os

v_eingabe_versuche = 0
while True:
    os.system("color F")
    os.system("cls")
    v_get_pw = open ('C:\FIAE\Apps\passwort.txt','r')
    #print(v_get_pw.readline(),"steht in der datei")
    v_passwort = v_get_pw.readline()
    #print(v_passwort, "Testzeile")
    print("Herzlich Willkommen zur Bank-o-Bank")
    print("Bitte PIN eingeben")
    v_pin = input(">>> ")
    v_eingabe_versuche += 1
    if v_pin == v_passwort:
        if v_pin == '1234':
            print('That password is one that an idiot puts on their luggage.')
            os.system('pause')
        break
    elif v_eingabe_versuche == 3:
        v_leer = " "
        v_text ="Alarm Alarm Alarm --- Zugriff verweigert --- Alarm Alarm Alarm"
        v_schleifenzähler = 0
        v_Rot = "4"
        v_Grün = "2"
        v_Gelb = "6"
        v_Blau = "1"


        while True:
            #time.sleep(0.05)
            v_farbe = random.randint(1,4)
            if v_farbe == 1:
                os.system("color "+ v_Rot)

            elif v_farbe == 2:
                os.system("color "+ v_Grün)

            elif v_farbe == 3:
                os.system("color " + v_Gelb)

            else:
                os.system("color "+ v_Blau)
            #print(v_farbe)
            os.system("cls")
            print ( (100 - v_schleifenzähler) * v_leer + v_text)
            v_schleifenzähler += 1
            if v_schleifenzähler > 90:
                v_schleifenzähler = 0
    else:
        print ('Falsche PIN Noch', 3- v_eingabe_versuche, 'Versuche')
        os.system('pause')




kontostand = 100  # 100€

while True:
    os.system("color F")
    os.system("cls") # Bildschirm säubern
    print("Hallo Max Mustermann")
    print("Ihr Kontostand beträgt:\t", kontostand, "€")
    print("Bitte wählen Sie:")
    print("[1] für Geld einzahlen")
    print("[2] für Geld abheben")
    print("[x] Programm beenden")
    eingabe = input(">>> ")
    
    if eingabe == "1":
        #os.system("color 2")
        while True:
            os.system("cls")
            print("Sie möchten Geld einzahlen")
            print("Bitte geben Sie den gewünschen Betrag an oder [x] zum abbrechen")
            eingabe = input(">>> ")
            
            if eingabe.isdecimal():
                eingabe = int(eingabe)
                kontostand = kontostand + eingabe
                print("Vielen Dank")
                os.system('pause')
                break
                
            elif eingabe == "x":
                print("Du kehrst jetzt in das Hauptmenü zurück.")
                os.system('pause')
                break
                
            else:
                print("Das habe ich nicht verstanden!")
                os.system('pause')
        
          
    elif eingabe == "2":
            #os.system("color 4")
            while True:
                os.system("cls")
                print("Sie möchten Geld abheben")
                print("Bitte geben Sie den gewünschen Betrag an oder [x] zum abbrechen")
                eingabe = input(">>> ")
                
                if eingabe.isdecimal():
                    eingabe = int(eingabe)
                    if eingabe > kontostand:
                        print (" Tut mir leid Sie Sind nicht Kreditwürdig")
                        os.system('pause')
                        break
                    else:
                        kontostand = kontostand - eingabe
                        print("Vielen Dank")
                        os.system('pause')
                        break
                    
                elif eingabe == "x":
                    print("Du kehrst jetzt in das Hauptmenü zurück.")
                    os.system('pause')
                    break
                    
                else:
                    print("Das habe ich nicht verstanden!")
                    os.system('pause')
    
    
    elif eingabe == "x":
        print("Auf Wiedersehen!")
        exit()
    
    
    else:
        print("Das habe ich nicht verstanden!")
        os.system('pause')
    
