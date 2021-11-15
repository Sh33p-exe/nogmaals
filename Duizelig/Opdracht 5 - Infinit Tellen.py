checken = True
aantal=0

while checken:
    aantal+=1
    vraag = input("zolang je geen quit in type zal het blijven vragen: ")
    if vraag !="quit":
        print("probeer nogmaal")
    else:
        print("u heeft",aantal,"keer geprobeert") 
        checken = False 

