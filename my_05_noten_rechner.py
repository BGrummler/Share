punkte=int(input("Wieviele Punkte hat der Schüler erreicht?: "))
if punkte < 0:
    print("\nUngültige Eingabe: ",punkte)
elif punkte < 35:
    print("\nDer Schüler bekommt eine 6\n")
elif  punkte < 50:
    print("\nDer Schüler bekommt eine 5\n")
elif  punkte < 60:
    print("\nDer Schüler bekommt eine 4\n")
elif  punkte < 75:
    print("\nDer Schüler bekommt eine 3\n")
elif  punkte < 85:
    print("\nDer Schüler bekommt eine 2\n")
elif  punkte <= 100:
    print("\nDer Schüler bekommt eine 1\n")
else:
    print("\nUngültige Eingabe: ", punkte)