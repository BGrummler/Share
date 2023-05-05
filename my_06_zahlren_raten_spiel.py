""" 
ZAHLEN-RATE-SPIEL
"""
import random
var_continue = True # variablen ob der Nutzer weiterspielen möchte und für den Punktestand
var_runde = 0
var_siege = 0
var_niederlagen = 0
versuch = 1

while var_continue: # while loop fragt nach jedem cyclus ob der nutzer weiter spielen möchte.
    if var_runde == 0: # wenn erstes spiel 
        var_runde += 1
        var_question = input("\nWollen wir ein Spiel spielen [j]a oder [n]ein?: ")
        var_continue = var_question == str.lower("j")
    else: 
        var_runde += 1 # wenn folgespiel nach continue fragen
        var_question = input("\nNoch eine Runde [j]a oder [n]ein?: ")
        var_continue = var_question == str.lower("j")
    if var_continue: # überprüfen ob der nutzer spielen / weiterspielen möchte
        bot_nr = random.randint(1, 10) # zufälliger int zw. 1 und 10
        while versuch < 3:#schleife die je nach anzahl versuchen erlaubt erneut zu raten.
            #print("Bitte eine Zahl zwischen 1 und 10 eingeben.")
            usr_nr = 0 # variable für Zahlenraten
            
 # TODO:try and except error for anything but integer input           
            while usr_nr < 1 or usr_nr > 10: # scheife wenn nutzer falsche zahl eingibt
                usr_nr = int(input("\nBitte eine Zahl zwischen 1 und 10 eingeben: "))
                if usr_nr > 0 and usr_nr < 11: # break bei korrekter eingabe
                    break
                else:
                    print("Falsche Eingabe") # ausgabe bei falscher eingabe -> eingabeschleife wird wiederholt
        
            if bot_nr == usr_nr: # überprüfen ob richtig geraten dann gewonnen
                print("Du hast gewonnen!")
                var_siege += 1
                versuch = 1
                break
            
            elif 1 < versuch: # überprüfen ob alle versuche verbraucht sind
                print("Leider Verloren, der Computer hatte eine: ", bot_nr,"\n")
                var_niederlagen += 1
                break
            else: # wenn zahl falsch geraten war aber noch versuche übrig sind
                versuch = versuch + 1
            
                if usr_nr > bot_nr: # prüfen ob zu hoch oder zu diedrig geraten wurde und hisweis geben
                    print("Die gesuchte Zahl ist kleiner!")
                else:
                    print("Die gesuchte Zahl ist größer!")
    else: # wenn der nutzer nicht mehr weiterspielen möchte werden statistiken angezeigt
        print("\nNach", var_runde-1, "Runde(n) steht es", var_siege, "Sieg(e) zu", var_niederlagen, "Niederlage(n), Auf Wiedersehen")
            
            
"""
Erweitere das Programm:
- Die Meldungen:
  - Zahl muss zwischen 1 und 10 liegen
  - Gesuchte Zahl ist größer/kleiner
  sollen nur erscheinen, wenn man sich im ersten Versuch
  befindet.
- Die Meldung:
  - Du hast verloren
  soll nur erscheinen, wenn man sich im letzten versuch
  befindet und falsch geraten hat

"""
        
        
        


