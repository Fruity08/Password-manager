def readpass(Namn):
    with open("password.csv", "r") as file :
        for line in file :
            if Namn in line:
                
                return(line.split(" "))