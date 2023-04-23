import os
l_money =[500]

def f_karten_mischen(v_Farben,v_Werte):
    import random
    v_Anzahl_Farben = len(v_Farben) #4 aber variabel
    v_Anzahl_Karten = v_Anzahl_Farben* (v_Werte[-1] + 1) # 52 Karten bei 13 * 4
    v_alle_karten = list(range(v_Anzahl_Karten)) # liste 0 bis 51
    return random.sample(v_alle_karten,v_Anzahl_Karten) # random funktion mischt die liste 51 integer

def f_table(d_ascii_karten, d_hands, v_turn): # ascii-art karten strings ,v_turn bestimmt wer karte bekommt
    d_ascii_karten[v_turn][0] = d_ascii_karten[v_turn][0] + ' _________ '
    d_ascii_karten[v_turn][1] = d_ascii_karten[v_turn][1] +'|' + str(d_hands[v_turn][-1][1]) +  '       |'
    d_ascii_karten[v_turn][2] = d_ascii_karten[v_turn][2] + '|    ' + str(d_hands[v_turn][-1][0]) + '    |'
    d_ascii_karten[v_turn][3] = d_ascii_karten[v_turn][3] + '|         |'
    d_ascii_karten[v_turn][4] = d_ascii_karten[v_turn][4] + '|_______'+ str(d_hands[v_turn][-1][1]) +  '|'
    return (d_ascii_karten)


def f_points(v_turn,v_wert,d_hands): # Punkteverteilung  (ALLES *100 weil floats unberechenbar sind)
    if 10 < v_wert <14: # 11, 12 & 13 also bube dame köning sind 1000
        v_wert = 1000
    elif v_wert == 1: # bestimmt ob Ass 1 oder 11 ist
        if d_hands[v_turn][0][1] %100 == 0: # wenn noch kein ass in der hand is ist der modulus 0
            v_wert = 1105 # ass ist 1105. dadurch ist die hand nacher x += 1105 und der modulus %100 ist 5 also nie wieder 0 
        else:
            v_wert = 100 # wenn schon ein ass in der hand (modulus != 0) ist ist jedes weitere Ass nur 100 wert
    else:
        v_wert = v_wert * 100 # 2 bis 10 sind 200 bis 1000
    return v_wert

def f_Karte(v_wert): #strings für ascii art
        if 1 < v_wert < 10:
            v_wert_string =' '+ str(v_wert) # 2 bis 9 wird mit leerzeichen ' 'als platzhalter  dargestellt
        elif v_wert == 10:
            v_wert_string = "10"
        elif v_wert == 11:
            v_wert_string = " B" # 11 = Bube
        elif v_wert == 12:
            v_wert_string = " D" # 12 = Dame
        elif v_wert == 13:
            v_wert_string = " K" # 13 = König
        elif v_wert == 1:
            v_wert_string = " A" # 1 = Ass
        return v_wert_string


def f_print_table(v_player_turn,v_turn,d_ascii_karten): # darstellung der karten
    os.system('cls')
    print(50*'_')

    if v_player_turn: # wenn der spieler am zug → 2te karte vom geber verdeckt von ascii_karten[2] dict
        print('Dealer')
        print(d_ascii_karten[2][0])
        print(d_ascii_karten[2][1])
        print(d_ascii_karten[2][3])
        print(d_ascii_karten[2][3])
        print(d_ascii_karten[2][2])
        print(d_ascii_karten[2][3])
        print(d_ascii_karten[2][3])
        print(d_ascii_karten[2][4])
        print(d_ascii_karten[2][5])
    else: # wenn dealer am zug wird alles angezeigt
        print('Dealer')
        print(d_ascii_karten[0][0])
        print(d_ascii_karten[0][1])
        print(d_ascii_karten[0][3])
        print(d_ascii_karten[0][3])
        print(d_ascii_karten[0][2])
        print(d_ascii_karten[0][3])
        print(d_ascii_karten[0][3])
        print(d_ascii_karten[0][4])
        print(d_ascii_karten[0][5])

    print('Player')# spieler hand wird immer angezeigt
    print(d_ascii_karten[1][0])
    print(d_ascii_karten[1][1])
    print(d_ascii_karten[1][3])
    print(d_ascii_karten[1][3])
    print(d_ascii_karten[1][2])
    print(d_ascii_karten[1][3])
    print(d_ascii_karten[1][3])
    print(d_ascii_karten[1][4])
    print(d_ascii_karten[1][5])

def f_blackjack():

    v_Farben = ("♦", "♣", "♥", "♠") # Farben
    v_Werte = list(range(13)) # Karten 1 bis 13 (Ass ist 1)  (!!!evtl überflüssig zahl 13 hätte gereicht!!!)
    l_burn_cards = []
    d_hands = {0:[['Dealer',0]], 1:[['Player',0]]} #dictionary für summe der hand werte [0][0][1] & [1][0][1] und hände [0][1](x,y) karten tupel x Farbe y wert
    d_ascii_karten = {0:['','','','','',''], 1:['','','','','',''], 2:['','','','','','']} #leere strings für karten ascii art
    v_burn_cards = 1 # anzahl karten die nach dem mischen direkt in den ablagestapel kommen, normal 1
    v_player_turn = True # True solange spieler Hit
    v_counter = 0 # um die ersten 4 karten auszuteilen
    v_game =""

    for v_oberste_karte in f_karten_mischen(v_Farben,v_Werte): #zieht oberste Karte im gemischten Deck bis Deck zuende ist
        v_oberste_karte_farbe = v_oberste_karte // 13 # berechnet farbe der obersten Karte 0 bis 51 // 13 sind 0 bis 3 !!!
        v_Farbe = v_Farben[v_oberste_karte_farbe] #  v_farben[0 bis 3 ] = "♦", "♣", "♥", "♠"
        v_oberste_karte_wert = (v_oberste_karte % 13 + 1) # berechnet wert der obersten karte 1 bis 13 bzw. Ass bis König
        v_wert = v_oberste_karte_wert # <- überflüssig , hätte auch mit v_oberste_karte_wert rechnen können oO

        if v_counter < v_burn_cards: # berechnung für burn cards
            l_burn_cards.append((v_Farbe,f_Karte(v_wert))) # burn cards ins dictionary eintragen
            v_counter += 1
            continue
            
        elif v_counter < 4 + v_burn_cards: #4 karten austeilen
            if v_counter % 2 != 0: # durch modulus 2 abwechselnd dealer → spieler → dealer → spieler
                v_turn = 0 # dealer bekommt die karte
                d_hands[0][0][1] = d_hands[0][0][1] + f_points(v_turn,v_wert,d_hands) # Summe der karten in der Hand aktualisieren
                d_hands[0].append((v_Farbe,f_Karte(v_wert))) # karte ins als tupel ins dictionary eintragen
                v_counter += 1
                d_ascii_karten = f_table(d_ascii_karten, d_hands, v_turn) # asci-art generieren
                if v_counter == 1 + v_burn_cards: # verdeckte geber hand generieren
                    d_ascii_karten[2][0] = d_ascii_karten[2][0] + ' _________ ' + ' _________ '
                    d_ascii_karten[2][1] = d_ascii_karten[2][1] +'|' + str(d_hands[v_turn][-1][1]) +  '       |' + '|?????????|'
                    d_ascii_karten[2][2] = d_ascii_karten[2][2] + '|    ' + str(d_hands[v_turn][-1][0]) + '    |' + '|?????????|'
                    d_ascii_karten[2][3] = d_ascii_karten[2][3] + '|         |' + '|?????????|'
                    d_ascii_karten[2][4] = d_ascii_karten[2][4] + '|_______'+ str(d_hands[v_turn][-1][1]) +  '|' + ' _________ '
            else:
                v_turn = 1 # spieler bekommt die karte
                d_hands[1][0][1] = d_hands[1][0][1] + f_points(v_turn,v_wert,d_hands) # summe der handkarten wird aktualisiert
                d_hands[1].append((v_Farbe,f_Karte(v_wert))) # karte wird als tupel ins dictionary eingetragen
                v_counter += 1
                d_ascii_karten = f_table(d_ascii_karten, d_hands, v_turn) # karte wird gemalt
        else:

            if d_hands[0][0][1] == 2105:
                v_player_turn = False
                f_print_table(v_player_turn,v_turn,d_ascii_karten)
                print('Dealer has Blackjack')
                v_game = 'loose'
                if d_hands[0][0][1] == d_hands[1][0][1]:
                    f_print_table(v_player_turn,v_turn,d_ascii_karten)
                    print('Both Blackjack')
                    v_game ='draw'
                    break
                break
            if d_hands[1][0][1] == 2105:
                f_print_table(v_player_turn,v_turn,d_ascii_karten)
                print('Player has Blackjack')
                v_game = 'Blackjack'
                break
            if d_hands[v_turn][0][1] >= 2200: # Bust
                if d_hands[v_turn][0][1] % 100 == 5: # ist ein Ass mit wert 1105 in der bust hand ?  ///    Ass + 7 + 5 = 23      /     2305 % 100 == 5
                    d_hands[v_turn][0][1] = d_hands[v_turn][0][1] - 999 # Ass abziehen                     ///    Ass + 7 + 5 = 13      /     2305 - 999 = 1306 → %100 != 0 oder 5
                else:
                    f_print_table(v_player_turn,v_turn,d_ascii_karten)
                    print(d_hands[v_turn][0][0], 'busts with', d_hands[v_turn][0][1]//100 ,'Points') # wenn der wert nicht auf 5 endet verloren
                    if d_hands[0][0][1] >= 2200:
                        v_game = "win"
                        break
                    elif d_hands[1][0][1] >= 2200:
                        v_game = "loose"
                        break

            if v_player_turn == True:
                if v_counter == 4 + v_burn_cards: 
                    '''
                    if d_hands[0][1][1] == ' A':                
                        f_print_table(v_player_turn,v_turn,d_ascii_karten)
                        v_player_insurance = input('enter [I] fir Insurance? :') ### <<<<<<<<<<<<<<<<<<<<<<< TODO add insurance here
                    if d_hands[1][1][1] == d_hands[1][2][1]:
                        v_player_split = input("enter [S] to Split !") ### <<<<<<<<<<<<<<<<<<<<<<< TODO Split
                        if v_player_split == str.lower('s'):
                            d_hands[v_turn+1] = ['Player',0] + d_hands.pop([1][0])
                            v_counter -= 1
                            del v_player_split
                            pass
                    '''

                v_counter += 1
                print(v_counter, v_burn_cards)
                f_print_table(v_player_turn,v_turn,d_ascii_karten)
                v_player_choice = input ('[H]it or [S]tay: ') # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Spieler entscheided ob noch eine karte 
                if v_player_choice == str.lower('h'):
                    v_turn = 1
                    d_hands[1][0][1] = d_hands[1][0][1] + f_points(v_turn,v_wert,d_hands)
                    d_hands[1].append((v_Farbe,f_Karte(v_wert)))
                    v_player_turn = True
                    d_ascii_karten = f_table(d_ascii_karten, d_hands, v_turn)
                else: 
                    v_turn = 0
                    v_player_turn = False 

            else:
                if d_hands[0][0][1] < 1699 or d_hands[0] ==  1705: # dealer muss unter weicher 17 ziehen. (17 mit ass, welches 11 wert ist)
                    d_hands[0][0][1] = d_hands[0][0][1] + f_points(v_turn,v_wert,d_hands)
                    d_hands[0].append((v_Farbe,f_Karte(v_wert)))
                    d_ascii_karten = f_table(d_ascii_karten, d_hands, v_turn)
                else:
                    if  d_hands[0][0][1] // 100  == d_hands[1][0][1] // 100:
                        f_print_table(v_player_turn,v_turn,d_ascii_karten)
                        print('Dealer hat', d_hands[0][0][1] // 100, 'Punkte')
                        print('Spieler hat: ', d_hands[1][0][1] // 100, 'Punkte')
                        print('Unentschieden')
                        v_game = "draw"    
                        os.system('pause') 
                        break        
                    elif d_hands[0][0][1]  > d_hands[1][0][1]:
                        f_print_table(v_player_turn,v_turn,d_ascii_karten)
                        print('Dealer hat', d_hands[0][0][1] // 100, 'Punkte')
                        print('Spieler hat: ', d_hands[1][0][1] // 100, 'Punkte')
                        print('Spieler  hat verloren')
                        v_game = "loose"
                        os.system('pause')
                        break
                    else:
                        f_print_table(v_player_turn,v_turn,d_ascii_karten)
                        print('Dealer hat', d_hands[0][0][1] // 100, 'Punkte')
                        print('Spieler hat: ', d_hands[1][0][1] // 100, 'Punkte')
                        print('Spieler hat gewonnen') 
                        v_game = "win"
                        os.system('pause')
                        break                            

    return v_game
               

while True:
    while True:
        os.system('cls')
        v_bet = input('Sie haben '+ str(l_money[0]) + ' Coin-O-Rhinos, bitte um Einsatz 2 bis 300: ')
        if v_bet.isdigit() and int(v_bet) <= l_money[0]:
            v_i_bet = int(v_bet)
            break
        else:
            print ('Falsche eingabe oder nicht genug Rhinos')

    v_result = f_blackjack()

    if v_result == 'blackjack':
        l_money[0] = l_money[0] + 1.5 * v_i_bet
    elif v_result == 'win':
        l_money[0] = l_money[0] +  v_i_bet
    elif v_result == 'loose':
        l_money[0] = l_money[0]  - v_i_bet
    else:
        pass
    if l_money[0] == 0:
        print('Sie sind Pleite')
        quit()
    v_s_q_another_round = input('Sie haben '+str(l_money)+' Coin-O-Rhinos, noch eine Runde [y] or [n] ?: ')
    if v_s_q_another_round == str.lower('y'):
        continue
    else:
        if l_money[0] >= 10000:
            print('unglaublich Sie haben das Kasino gesprengt, für die ', l_money, ' Rhinos kaufen Sie sich ein echtes Nashorn !')
            quit()
        elif l_money[0] >= 1000:
            print('wow Sie haben super gespielt und gehen mit ', l_money, ' Rhinos feiern')
        elif l_money[0] > 500:
            print('Sie haben gewonnen und gehen mit ', l_money, ' Rhinos nach Hause')
            quit()
        elif l_money[0] == 500:
            print('+-0 Sie gehen mit ', l_money, ' Rhinos , hoffentlich hatten Sie wenigstens Spass')
            quit()
        elif l_money[0]  < 500:
            print('Verloren, sie gehen mit nur ', l_money, ' Rhinos wieder nach Hause, dabei sein ist alles !')
            quit()
