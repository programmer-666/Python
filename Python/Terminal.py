#Son dosya - Kosullar
import os
from time import sleep
cmdcls = "cls"
os.system(cmdcls)
while True:
    print("CoreOS 0.0.1 - Base Terminal")
    while True:
        komut = input("$C ~:")
        if not komut:
            continue
        elif komut == "id":
            print(id(komut))
        elif komut == "tem":
            os.system(cmdcls)
        elif komut == "cik":
            exit()
        elif komut == "mx":
            for x in range(1,98):
                sleep(0.3)
                print(x**x)
        else:
            print("'{0}' Adın da bir komut yok".format(komut))
        
    