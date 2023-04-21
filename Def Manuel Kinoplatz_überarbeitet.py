

def findSeatNr(row, number):
    count = 0
    while True:
        if count+number > len(row):
            return "Leider sind nicht genug Plätze frei"
        elif count <= len(row) and row[count] == "X":
            count += 1
            print("step", count)
        elif row[count] == None and number == 1:
            row[count] = "X"
            return count+1
        else:
            if count+number <= len(row):
                print("mehr plätze?",count)
                seatcount=1
                while seatcount<= number:
                    if row[count+seatcount] == "X":
                        count+=1
                        print('row ist', row, 'seatcount ist ', seatcount)
                        print("reichen nicht",count)
                        break
                    elif row[count+seatcount] == None:
                        seatcount += 1
                        print("noch ist platz",count)
                        if seatcount == number:
                            filler = 0 
                            
                            while filler<= number:
                                row[count+filler]="X"
                                print('filler ist ',filler)
                                filler += 1
                            
                            return count+1

#kino_reihe = ["X", "X", "X", None, "X", None, "X","X", None, None]
kino_reihe = ["X", "X", "X", None, "X", None, "X", None, None, "X"]
#kino_reihe = ["X", None, "X", None, "X", None, "X", None, None, None]
#kino_reihe = ["X", "X", "X", None, None, None, "X", None, None, None]
#kino_reihe = ["X", "X", None, None, "X", None, "X", None, None, None]
#kino_reihe = ["X", "X", "X", "X", None, None, None, None, None, None]

print(len(kino_reihe))

eingabe = int(input('Plätze?: '))
print(findSeatNr(kino_reihe,eingabe))
