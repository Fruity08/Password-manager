import csv
import sys
from Saver import savepass
from Reader import readpass
import os
import time

#fråga om du vill spara eller läsa lösenord & logic
mode = input("Vill du spara eller läsa lösenord?""\n")

if(mode != "spara" or "läsa"):
    print("Error: Du skrev inte spara eller läsa.")
    time.sleep(2.5)
    os.execl(sys.executable, sys.executable, *sys.argv)

#kalla på savepass functionen
if (mode == "spara") :
    wnamn = input("vad vill du kalla lösenordet?""\n")
    lösenord = input("Vad är lösenordet""\n")
    print(savepass(wnamn, lösenord))
if (mode == "läsa") :
    rnamn = input("vad heter lösenordet du vill läsa?""\n")
    print(readpass(rnamn))