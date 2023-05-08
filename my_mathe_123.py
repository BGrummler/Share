
while True:
    v_eingabe = input("bis wieviel soll gezählt werden? :") 
    v_schleife = 0 
    v_nullen_am_ende = 10
    v_ergebnis = 0 
    if v_eingabe.isdigit(): 
        v_eingabe = int(v_eingabe)
        break 
    else:
        print("Falsche eingabe") 

while v_schleife < v_eingabe + 1: 
    v_schleife += 1 
    v_ergebnis = v_ergebnis * v_nullen_am_ende + v_schleife - 1 
    if v_schleife == v_nullen_am_ende:            
        v_nullen_am_ende = v_nullen_am_ende * 10  
    print(v_ergebnis)