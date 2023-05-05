#finde freie plätze im kino nach anforderung oder gebe aus es gibt keine

#1 den ersten freie Einzelplatz
#2. die ersten freien doppelplätze
# gib die platznummer aus



'''
2 * [None] = [None,None]
'''




'''
Testreihen ↓
'''
#l_kino_reihe = ['x', None, 'x', None, None]
#l_kino_reihe = ['x', 'x', 'x', 'x', 'x']
#l_kino_reihe = ['x', None, 'x', None, None, 'x', None, 'x', None, None, None, 'x']
################ 1    2    3    4    5    6    7    8    9    10    11   12   13   14   15    16    17    18    19   20    21   22 
l_kino_reihe = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', None, 'x', 'x', 'x', 'x', None, None, 'x', None, None, None, 'x', 'x']
#l_kino_reihe = ['x', None, None, None, 'x']
#l_kino_reihe = [None, 'x', None , None, 'x']
'''
Testreihen ↑
'''
print(l_kino_reihe.index(None))
while True:
    if l_kino_reihe.count(None) == 0: #wenn keine plätze frei
        print('Es sind leider keine Plätze mehr frei')
        break
    v_eingabe = input('wieviele plätze benötigen Sie?: ') # Frage an Kunden nach Bedarf
    if v_eingabe.isdigit() and 0 < int(v_eingabe) < 10: #übeprüfung ob eingabbe korrekt
        v_eingabe = int(v_eingabe) 
    else:
        print('Falsche eingabe !')
        continue
    l_search = v_eingabe * [None] # umwandlung der eingabe in Liste zB 2 * [None] = [None, None]
    string_suchen = str(l_search) # convertiert die erstelle liste in einen string zB: '[None, None]'
    string_suchen = string_suchen[1:-1] # schneidet die klammern ab = 'None, None'
    if str(l_kino_reihe).count(string_suchen) == 0: #sucht ob substring im string ist
        print('Es sind leider keine Plätze ', v_eingabe, 'nebeneinander mehr frei')
        continue
    v_sitznummern = str(l_kino_reihe).index(string_suchen) # welche postition ist der string
    v_index = str(l_kino_reihe)[:v_sitznummern].count(',') # zählt anzahl kommas im string bis zur position des substrings
    print('Ihre Plätze befinden sich in Reihe 1, Platz Nummer ', v_index + 1, 'bis', v_index + v_eingabe)
    break
    
'''
while True:
    if l_kino_reihe.count(None) == 0:
        print('Es sind leider keine Plätze mehr frei')
        exit()
    v_eingabe = input('wieviele plätze benötigen Sie 1 oder 2: ?')
    if v_eingabe.isdigit() and 0 < int(v_eingabe) < 3:
        v_eingabe = int(v_eingabe)
    else:
        print('Falsche eingabe !')
        continue
    if v_eingabe == 1:
        print('der erste freie platz befindet sich in Reihe 1 Platz ',l_kino_reihe.index(None)+1)
        exit()
    elif v_eingabe == 2:
        i = 0
        while i < len(l_kino_reihe):
            if l_kino_reihe[i] == None and l_kino_reihe[i+1] == None:
                print('Die ersten freien Plätze sind ', i + 1, 'und', i + 2)
                exit()
            i += 1
        print('Es sind leider keine Doppelplätze mehr verfügbar')
        break
'''