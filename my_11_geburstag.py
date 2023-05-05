def f_geburtsdatum(frage,x,y):
    while True:
        eingabe = input(frage)     
        if eingabe.isdecimal() and x <= int(eingabe) <= y :
            print("Vielen Dank!")
            return int(eingabe)
        else:
            print("Das ist keine valide Eingabe!")

def f_alter(t,m,j):
    v_jahre = 2023 - int(j)
    if t > 17:
        m += 1
    if m > 4:         
        v_jahre -= 1
    return v_jahre   

# 1) Eingabe des Geburtstags
#    - Min: 1
#    - Max: 31
t = f_geburtsdatum('1) Eingabe des Geburtstags: ',1,31)
# 2) Eingabe des Geburtsmonats
#    - Min: 1
#    - Max: 12
m = f_geburtsdatum('2) Eingabe des Geburtsmonats: ',1,12)
# 3) Eingabe des Geburtsjahres
#    - Min: 1900
#    - Max: 2022
j = f_geburtsdatum('3) Eingabe des Geburtsjahres: ',1900,2022)

#print(str(t)+"."+str(m)+"."+str(j))
print(f"{t:02}.{m:02}.{j}")
print('du bist' ,f_alter(t,m,j))