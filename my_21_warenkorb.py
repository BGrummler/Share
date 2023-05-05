"""
Schreibe ein Programm, welches für einen 
gegebenen Warenkorb folgendes berechnet:
1) Anzahl der Artikel
  - beachte die Anzahl jedes einzelnen Artikels
  - im Beispiel = 8
2) Gesamtpreis des Warenkorbs
  - beachte die anzahl jedes einzelnen Artikels
  - Im Beispiel = 2399 * 2 + 1999 * 4 + 29999 * 2

BONUS)
- Teuerster Artikel
  - beachte die Anzahl jedes einzelnen Artikels
- Günstigster Artikel
  - beachte die Anzahl jedes einzelnen Artikels
"""

warenkorb = [
#   [<name>    , <preis>, <anzahl>]
    ["Tastatur", 2399, 2],
    ["Maus", 1999, 4],
    ["Monitor", 29999, 2]
]
preis  = 0
anzahl_artikel = 0
teuerster_artikel= ['',0,0]
g_artikel= ['',float('inf'),0]
for elem in warenkorb:
    preis += elem[1] * elem[2]
    anzahl_artikel += elem[2]
    if elem[1] > teuerster_artikel[1]:
        teuerster_artikel = elem
    elif elem[1] == teuerster_artikel[1]:
        teuerster_artikel.append(elem[1])
        g_artikel.append(elem[1])
    if elem[1] < g_artikel[1]:
        g_artikel = elem
    elif elem[1] == g_artikel[1]:
        g_artikel.append(elem[1])



print('Der Einkauf kostet ',preis/100,' €')
print('Es sind ',anzahl_artikel, ' Artikel')
print ('Der teuerste Artikel ist', teuerster_artikel[0])
print ('Der günstigste Artikel ist', g_artikel[0])