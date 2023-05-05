"""
Erzeuge folgendes Muster mithilfe einer while-Schleife:

*
**
***
****

Die Anzahl der "*" in der letzten Reihe hängt von der 
Variable `anzahl` ab.


v_anzahl_gesamt = 4
v_anzahl_jetzt = 0

while v_anzahl_jetzt < v_anzahl_gesamt :
    v_anzahl_jetzt += 1
    print (v_anzahl_jetzt * "*" )
    


Erzeuge folgendes Muster mithilfe einer while-Schleife:

1
12
123
1234

Die letzte Zahl in der letzten Zeile hängt von der Variable
`anzahl` ab.


anzahl = 4
"""
v_anzahl_gesamt = 4
v_anzahl_jetzt = 0
v_string_jetzt = ""

while v_anzahl_jetzt < v_anzahl_gesamt + 1 :
    v_anzahl_jetzt += 1 # 1 2 3 4 
    print (v_string_jetzt) # ""  "1" "12" "123" "1234"...
    v_string_jetzt = v_string_jetzt + str(v_anzahl_jetzt) # "" + "1" = "1" ; "1" + "2" = "12" ; "12" + "3" = "123" ...
