import random
import time
from datetime import datetime

now1 = datetime.now()
dt_string1 = now1.strftime("%H:%M:%S")
Password = "ABC"
list(Password)
Count = len(Password)
Dict = []
Try = True
Run = True

if Count == 2:

    with open("TwoCharDict.txt") as file:
        lines = [line.strip() for line in file]
        Dict.append(lines)
        
if Count == 3:

    with open("ThreeCharDict.txt") as file:
        lines = [line.strip() for line in file]
        Dict.append(lines)

while Run is True:

    try:
        Rand = random.choice(lines)
    except IndexError:
        pass
    str(Rand)
    print(Rand)

    if Rand == Password:
            print("")
            print("--------------------")
            print("")
            print("Solved!")
            print("Guess:" + Rand)
            print("Password:" + Password)
            now2 = datetime.now()
            dt_string2 = now2.strftime("%H:%M:%S")
            print("Start Time:", dt_string1)
            print("End Time:", dt_string2)
            Try = False
            Run = False
            break
    else:
        lines.remove(Rand)
        print("Removed:" , Rand , "from combos")
