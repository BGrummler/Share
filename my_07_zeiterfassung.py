"""
Entwickle ein Zeiterfassungsprogramm

Dabei soll der Nutzer für einen bestimmten Zeitraum
eintragen, wieviel er pro Tag gearbeitet hat.

Betrachtet wird der Zeitraum 01.03.2023 bis 04.03.2023.

Pro Tag gibt der Nutzer die geleistete Arbeitszeit ein
(z.B. 8 für Acht Stunden)

Anschließend wird die Summe der Arbeitszeiten gebildet & ausgegeben
und die durchschnittlich gearbeitete Zeit ausgegeben

Benötigt wird eine Nutzereingabe für die es bestimmte Bedingungen gibt:
- str.isdecimal() um zu prüfen, ob die Nutzereingabe NUR aus Zahlen besteht
  (z.B.
   eingabe = input("Arbeitszeit: ")
   print(eingabe.isdecimal()) # wenn True, dann hat Nutzer nur Zahlen eingegeben
- Die Arbeitszeit muss über 0 Stunden liegen
- Die Arbeitszeit darf nicht höher als 10 Stunden liegen
"""



var_summe = 0
var_counter = 1
while var_counter < 5:
    while True:
        print("\nFür den 0", var_counter, ".03.2023",sep="")
        var_eingabe_stunden = input("Bitte geleistete Arbeitsstunden 1 bis 10 eingeben: ")
        if var_eingabe_stunden.isdecimal() and 0 < int(var_eingabe_stunden) < 11:
            var_eingabe_stunden = int(var_eingabe_stunden)
            break
        else:
            print ("\nFalsche Eingabe !")
    
    var_summe = var_summe + var_eingabe_stunden
    var_counter = var_counter + 1
   
print("Summe der Arbeitszeit:", var_summe, "Stunden")
print("Durchschnittliche Arbeitszeit pro tag:", var_summe/(var_counter-1),"Stunden")
