"""
Welche Datentypen sollten für die folgenden 
Anforderungen gewählt werden?
"""

"""
a) Es soll eine zentrale Sammlung aller Mitarbeiterdaten existieren. 
   Zu jedem Mitarbeiter stehen folgende Informationen zur Verfügung:
    - Mitarbeiter Id    (Integer)   Set
    - Nachname          (String)    Tupel
    - Vorname           (String)    Tupel
    - Geburtsjahr       (Integer)   Tupel
    - Gehalt            (Float)     Liste

    dict !
"""
mitarbeiterdaten ={
   1:["Mustermann", "Manuela", 1987, 4834.74 ],
   2:["Wayne", "John", 1946, 2597.87]
                  }


"""
b) Es sollen die Ergebnisse einer Abschlussprüfung ohne Personenbezug 
   gespeichert werden. 
   Die Ergebnisse sind Ganzzahlen in 5er Schritten 
   (z.B. 5, 10, 15, 20 etc.) bis maximal 100.   
   
   Tupel
"""
Ergebnisse = (5, 95, 100, 95, 55, 75, 5, 95)
"""
c) Es soll ein Login-Protokoll geführt werden. 
   Dabei gibt es pro Login-Versuch folgende Informationen:
    - E-Mail-Adresse                (String)       
    - War der Login erfolgreich?    (Boolean)      
    
    Liste aus tuple 
"""
login_protokoll = [("a@b.cd",0),("b@c.de",1),("a@b.cd",1)]

"""
Definiere eine Funktion, welche überprüft, ob die Datentypen der
Elemente eines Tuples gleich sind

Die Funktion erhält als Parameter eine Variable vom Typ Tupel.

Die Funktion gibt...
-> True zurück, wenn alle Elemente den gleichen Datentypen haben
-> False zurück, wenn nicht
"""
x = ([],[1],[2])

def f_is_same_type(object_to_check):
   
   if len({type(elem) for elem in object_to_check}) < 2: # type(elem for elem in x) = class generator ??? generiert eine liste wenn eingeklammert = ()[]{}
      return True                                        # gibt speicheradresse zurück wenn in str(), kann nicht alleine stehen ?
   else:
      return False
        
if f_is_same_type(x):
    print("das Objekt hat keine unterschiedlichen Datentypen")
else:
    print("das Objekt hat unterschiedlichen Datentypen")


"""
Definiere eine Funktion, welche die einzigartigen Zeichen
eines strings zählt und den Wert als int zurückgibt

Anmerkung: Klein- und Großbuchstaben sind unterschiedliche Zeichen!

"Python"  -> 6
"Pythonn" -> 6
"pPython" -> 7
"""
test_string = "Warum darf man Nachts nicht unterm Kirschbaum stehen ?"

def f_count_unique(string_to_check):
   return len(set(string_to_check))

print(f_count_unique(test_string)*3)

"""BONUS)
Definiere eine Funktion, welche die Vokale eines strings entfernt.

Vokale sind die Buchstaben a e i o u bzw. A E I O U

Die Funktion erhält als Parameter einen string

Die Funktion gibt zurück:
- einen string (aber ohne Vokale)

Beispiel:
"abce" -> "bc"
"ae"   -> ""
"xyz"  -> "xyz"
"""
def f_remove_vocal(string_to_manipupulate):
   _ = {'a','e','i','o','u','A','E','I','O','U'}
   new_string =''
   for elem in string_to_manipupulate:
      if elem not in _:
         new_string += elem
   return new_string

print(f_remove_vocal(test_string))
