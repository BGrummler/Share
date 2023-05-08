l_ttt = 9 * [None] #liste generieren
l_chance=0
print (l_ttt,'\n\n')

#l_ttt[0] = ' >< '
#l_ttt[1] = ' >< '
#l_ttt[2] = ' >< '

def f_male_spielfeld( l_ttt ): # ascii art aus der liste
    print(l_ttt[0],'|',l_ttt[1],'|',l_ttt[2])
    print(18*'-')
    print(l_ttt[3],'|',l_ttt[4],'|',l_ttt[5])
    print(18*'-')
    print(l_ttt[6],'|',l_ttt[7],'|',l_ttt[8])


def f_spiel_ende(l_ttt): # true wenn gewonnen
    for i in range(0,2):
        if l_ttt[i*3] == l_ttt[i*3+1] ==l_ttt[i*3+2] and l_ttt[i*3] != None :
            return True
        elif l_ttt[i] == l_ttt[i+3] ==l_ttt[i+6] and l_ttt[i] != None :
            return True
    if l_ttt[0] == l_ttt[4] ==l_ttt[8] and l_ttt[4] != None :
        return True
    elif l_ttt[6] == l_ttt[4] ==l_ttt[2] and l_ttt[4] != None :
        return True
    else:
        return False

def f_freie_felder(l_ttt):
    l_der_freien_felder = []
    for i,elem in enumerate(l_ttt):
        if elem == None:
            l_der_freien_felder.append(i)
    return l_der_freien_felder

def f_computer_ai(l_spielstand,l_chance):
    for f_feld in f_freie_felder(l_spielstand):
        #print(l_spielstand)
        l_neuer_spielstand = l_spielstand.copy()
        #print(l_neuer_spielstand.count(None))
        if l_neuer_spielstand.count(None) % 2 == 0:
            l_neuer_spielstand[f_feld] = ' () '
        else:
            l_neuer_spielstand[f_feld] = ' >< '

        if f_spiel_ende(l_neuer_spielstand):
            print ('\n',l_neuer_spielstand[:3],'\n',l_neuer_spielstand[3:6],'\n',l_neuer_spielstand[6:],'\n')
            print('anzahl leere felder : ',l_neuer_spielstand.count(None),'\nam zug ist: ',l_neuer_spielstand.count(None)%2)
            if l_neuer_spielstand.count(None) % 2 == 0:
                if l_chance < l_neuer_spielstand.count(None):
                    l_chance = l_neuer_spielstand.count(None)

            else:
                if l_chance > l_neuer_spielstand.count(None) * -1:
                    l_chance = l_neuer_spielstand.count(None) * -1

            print(l_neuer_spielstand.count(None)%2,' hat gewonnen l_chance ist ', l_chance)
            return l_chance
                
        else:
            f_computer_ai(l_neuer_spielstand,l_chance)
            if f_computer_ai(l_neuer_spielstand,l_chance) == None: ### TODO
                f_computer_ai(l_neuer_spielstand,l_chance) ### TODO
            else:
                return f_computer_ai(l_neuer_spielstand,l_chance) ### TODO l_chance ### TODO
                        
def game_ttt(l_ttt):
    if l_ttt.count(None) % 2 != 0:
        f_male_spielfeld(l_ttt)
        v_spieler_zug = input('\n\nBitte X setzen:\n\n1|2|3\n4|5|6\n7|8|9\n\n>>> ')
        if v_spieler_zug in ['1','2','3','4','5','6','7','8','9'] and l_ttt[int(v_spieler_zug) -1] == None:
            l_ttt[int(v_spieler_zug) -1] = ' >< '
            game_ttt(l_ttt)
        else:
            print('ungültige eingabe')
            game_ttt(l_ttt)

        if f_spiel_ende(l_ttt):
            print('gewonnen spieler')
            exit()
    else:
        f_computer_ai(l_ttt, l_chance)
        print('Der Computer wählt: ', f_freie_felder(l_ttt)[0])
        l_ttt[f_freie_felder(l_ttt)[0]] = ' () '
        game_ttt(l_ttt)

        if f_spiel_ende(l_ttt):
            print('gewonnen computer')
            exit()


game_ttt(l_ttt)
f_male_spielfeld(l_ttt)



