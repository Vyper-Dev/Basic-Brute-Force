import random
import time
from datetime import datetime

dt_string1 = datetime.now().strftime("%H:%M:%S")
Password = "AB"
list(Password)
Dict = []

if len(Password) == 2:
    with open("TwoCharDict.txt") as file:
        lines = [line.strip() for line in file]
        Dict.append(lines)
if len(Password) == 3:
    with open("ThreeCharDict.txt") as file:
        lines = [line.strip() for line in file]
        Dict.append(lines)

while True:
    Rand = random.choice(lines)
    if Rand == Password:
            print("\n--------------------")
            print(f"Password: {Password}")
            dt_string2 = datetime.now().strftime("%H:%M:%S")
            print(f"Start Time: {dt_string1} \nEnd Time: {dt_string2}")
            break
    else:
        lines.remove(Rand)