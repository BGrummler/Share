SP = int(input("\nWieviele Spieltage: "))
spieltage = 0
siege = 0
unentschieden = 0
niederlagen = 0
toregesamt = 0
gegentoregesamt = 0
while spieltage != SP:
    print("\nSpieltag: ",spieltage + 1, " von ", SP )
    tore, gegentore = input(" Tore:Gegentore ").split(":")
    tore = int(tore)
    gegentore = int(gegentore)
    #print (tore, " : ", gegentore)
    spieltage+=1
    toregesamt += tore
    gegentoregesamt += gegentore
    if tore>gegentore:
        siege += 1
    elif tore==gegentore:
        unentschieden += 1
    else:
        niederlagen += 1
tordifferenz = toregesamt - gegentoregesamt
print("\nSpiele:", spieltage, "| Siege:", siege, "| Unentschieden:", unentschieden,"| Niederlagen:", niederlagen,  "| Tore:",  toregesamt, "| Gegentore:", gegentoregesamt, "|Tordifferenz: ", tordifferenz,"| Punkte:", siege*3+unentschieden )
