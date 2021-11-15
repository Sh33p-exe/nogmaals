getal = 1 
tijd = "AM"


while getal <=12:
    print(getal , tijd)
    if getal ==12 and tijd == "AM":
        getal =0
        tijd = "PM"
    getal+=1