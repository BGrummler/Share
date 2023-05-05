"""
Erstelle ein CLI-Tool mit dem sich ein Nutzerprofil darstellen lässt

Hole zunächst folgende Informationen vom Nutzer:
1) Name
   - Ein Name muss aus mind. 3 Zeichen bestehen
   - Ein Name darf keine Zahlen enthalten
2) Geburtsjahr
   - Es muss ein valides und "realistisches" Geburtsjahr sein
   - Das Mindestalter zur Nutzung des Programms ist 18
3) Wohnort
   - Ein Wohnort muss aus mind. 5 Zeichen bestehen
   - Ein Wohnort darf keine Zahlen enthalten
   
Anschließend kann der Nutzer über ein Menü:
- Seinen Namen verändern
  (beachte die Namens-Regeln!)
- Sein Geburtsjahr verändern
  (beachte die Geburtsjahr-Regeln!)
- Seinen Wohnort verändern
  (beachte die Wohnort-Regeln!)
- Programm beenden

Tipp: Verwende die len()-Funktion
"""
V_Frage_Name = "Bitte Name eingeben\n\
   - Ein Name muss aus mind. 3 Zeichen bestehen\n\
   - Ein Name darf keine Zahlen enthalten \n\
>>> "
V_Frage_Geburtsjahr = "Bitte Geburtsjahr eingeben \n\
   - Es muss ein valides und \"realistisches\" Geburtsjahr sein\n\
   - Das Mindestalter zur Nutzung des Programms ist 18\n\
>>> "
V_Frage_Geburtsort = "3) Wohnort\n\
   - Ein Wohnort muss aus mind. 5 Zeichen bestehen\n\
   - Ein Wohnort darf keine Zahlen enthalten\n\
>>> "
V_Menu = "Sind diese eingaben korrekt ? \n\
    1 für Name ändern\n\
    2 für Geburtsjahr ändern\n\
    3 für Wohnsitz ändern\n\
    4 für beenden\n\
>>> "
V_Länge_Name = 2
V_Länge_Wohnort = 4
v_welche_frage = 0
v_name =""
v_jahrgang =""
v_wohnort =""
import os
while True:
  os.system("cls")
  if v_welche_frage == 0:
    v_frage = V_Frage_Name
  elif v_welche_frage == 1:
    v_frage = V_Frage_Geburtsjahr
  elif v_welche_frage == 2:
    v_frage = V_Frage_Geburtsort
  else:
    v_frage = V_Menu
    print("Hallo", v_name, "bitte überprüfe deine Eingabe.\n\
Dein Geburtsjahr ist: ", v_jahrgang, "\n\
Wohnsitz in: ", v_wohnort,)
  v_input = input(v_frage)
  if v_welche_frage == 0 and v_input.isalpha() and len(v_input) > V_Länge_Name:
    v_name = v_input
    if v_jahrgang == "":
      v_welche_frage = 1
    else:
      v_welche_frage = 3
  elif v_welche_frage == 1 and v_input.isdigit() and 1900 < int(v_input) < 2003:
    v_jahrgang = v_input
    if v_wohnort == "":
      v_welche_frage = 2
    else:
      v_welche_frage = 3
  elif v_welche_frage == 2 and v_input.isalpha() and len(v_input) > V_Länge_Wohnort:
    v_wohnort = v_input
    v_welche_frage = 3
  elif v_welche_frage ==3:
    if v_input == "1":
        v_welche_frage = 0
    elif v_input == "2":
        v_welche_frage = 1
    elif v_input == "3":
        v_welche_frage = 2
    else:
      os.system("cls")
      print("Auf Wiedersehen")
      quit()
  else:
    print(v_frage, "ist falsch")