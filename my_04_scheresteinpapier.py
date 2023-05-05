import random
eingabe = input("Schere, Stein oder Papier?: ")
computer = random.choice(["Schere","Stein", "Papier"])
print("\nDu hast", eingabe, "Der Computer hat", computer,"\n")
if eingabe ==  computer:
    print("Unentschieden")
elif eingabe == "Schere" and computer == "Papier":
    print("Gewonnen")
elif eingabe == "Stein" and computer == "Schere":
    print("Gewonnen")
elif eingabe == "Papier" and computer == "Stein":
    print("Gewonnen")
else:
    print("Verloren")