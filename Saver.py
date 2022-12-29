def savepass(Namn, Lösen):
    #Spara lösenord 
    password = Namn+" "+Lösen
    password = password+'\n'
    with open("password.csv", "a") as file :
        file.write(password)
    return("Klar")