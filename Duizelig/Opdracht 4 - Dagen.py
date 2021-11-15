dag = input("welke dagen wil je opvragen? ma di wo do vr za zo? ")
deur = 1
check = False

while not check:
    if deur == 1:
        print("maandag")
        dagen = "ma"
        deur = 2
    elif  deur == 2:
        print("dinsdag")
        dagen = "di"
        deur = 3
    elif deur == 3:
        print("woensdag") 
        dagen ="wo"
        deur = 4
    elif deur == 4:
        print("donderdag")
        dagen ="wo"
        deur = 5
    elif deur == 5:
        print("vrijdag")
        dagen ="vr"
        deur = 6
    elif deur == 6:
        print("zaterdag")
        dagen ="za"
        deur =7
    elif deur == 7:
        print("zondag")
        dagen ="zo"
    check = dag == dagen