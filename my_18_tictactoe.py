"""
Entwickle ein Programm, um für ein gegebenes TicTacToe-Spielfeld
einen Sieger bzw. ein Unentschieden zu ermitteln.
"""

import os
import random
v_game = True
l_tictactoe = [['','',''],['','',''],['','','']]

def f_table():
    print(f'''
         A    B    C
      ┏━━━━┳━━━━┳━━━━┓
    1 ┃ {l_tictactoe[0][0]:3}┃ {l_tictactoe[0][1]:3}┃ {l_tictactoe[0][2]:3}┃
      ┣━━━━╋━━━━╋━━━━┫
    2 ┃ {l_tictactoe[1][0]:3}┃ {l_tictactoe[1][1]:3}┃ {l_tictactoe[1][2]:3}┃
      ┣━━━━╋━━━━╋━━━━┫
    3 ┃ {l_tictactoe[2][0]:3}┃ {l_tictactoe[2][1]:3}┃ {l_tictactoe[2][2]:3}┃
      ┗━━━━┻━━━━┻━━━━┛    
    ''')

def f_check_win(a,b,c,d,e,f):
    if l_tictactoe[a][b] == l_tictactoe[c][d] == l_tictactoe[e][f] and l_tictactoe[a][b] != "":
        if l_tictactoe[a][b] == "O":
            f_table()
            print("Du hast gewonnen")
        else:
            f_table()
            print("Du hast verloren")       
        return True

os.system('cls')

_ = input('möchtest du Anfangen [j] oder [n]?: ')

if _ == str.lower('j'):
    v_wer_ist_dran = "O"
    print("TicTacToe")
else:
    v_wer_ist_dran = "X"

while True:
    for i in range (3):
        if f_check_win(i,0,i,1,i,2,):
            v_game = False
            break

        if f_check_win(0,i,1,i,2,i,):
            v_game = False
            break

    if f_check_win(0,0,1,1,2,2):
            v_game = False
            break
  
    if f_check_win(2,0,1,1,0,2):
            v_game = False
            break
   
    if v_game == False:
        break
    
    if v_wer_ist_dran == "O":
        f_table()
        v_Input = input('Bitte Feld angeben: ')

        if len(v_Input) == 2 and str.lower(v_Input[0]) in "abc" and v_Input[1] in "123":
            os.system('cls')

            if str.lower(v_Input[0]) == "a":
                v_zuweisung_zwei = 0
            elif str.lower(v_Input[0]) == "b":
                v_zuweisung_zwei = 1
            else:
                v_zuweisung_zwei = 2

            if l_tictactoe[int(v_Input[1])-1][v_zuweisung_zwei] == "":   
                l_tictactoe[int(v_Input[1])-1][v_zuweisung_zwei] = "O"
                print('Spieler: '+ str.upper(v_Input[0])+ v_Input[1])
                v_wer_ist_dran = "X"
                continue
            else:
                print('Feld '+ str.upper(v_Input[0])+ v_Input[1]+ ' schon belegt')

        elif str.lower(v_Input) == "q":
            print('auf wiedersehen')
            quit()
        else:
            print('Falsche Eingabe')
            continue

        if '' not in l_tictactoe[0] and '' not in l_tictactoe[1] and '' not in l_tictactoe[2]:
            print("Unentschieden")
            break

    if v_wer_ist_dran == "X":
        while True:
            v_i_computer_wurf = random.randint(0,2)
            c_a_computer_buchstabe = random.choice('abc')

            if str.lower(c_a_computer_buchstabe) == "a":
                v_zuweisung_zwei = 0
            elif str.lower(c_a_computer_buchstabe) == "b":
                v_zuweisung_zwei = 1
            else:
                v_zuweisung_zwei = 2

            if l_tictactoe[v_i_computer_wurf][v_zuweisung_zwei] == "":
                l_tictactoe[v_i_computer_wurf][v_zuweisung_zwei] = "X"
                print('Computer: ' + str.upper(c_a_computer_buchstabe) + str( v_i_computer_wurf + 1))
                v_wer_ist_dran = "O"
                break
            else:
                continue 