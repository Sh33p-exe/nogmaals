checken = True
aantal=0

while checken:
    aantal+=1
    stop = input("Vul 'quit' in om deze zin te stoppen, zolang je dit niet doet zal deze zin zig erhalen: ")
    if stop !="quit":
        print("probeer het nog een keer")
    else:
        print("je hebt het ",aantal,"keer geprobeert") 
        checken = False 