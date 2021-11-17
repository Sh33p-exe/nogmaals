# name of student: Quinten van de Weg
# number of student:
# purpose of program: Kassa
# function of program: 
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #erugbetalen 
paid = int(float(input('Paid amount: ')) * 100) #Bedrag die al betaald is
change = paid - toPay #Bedrag die je moet terug geven aan de klant

if change > 0: # Als je wel moet terugbetalen gaat hij de coins aangeven
  coinValue = 500 # Bij welke coin hij begint
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('Al het geld terug gegeven')