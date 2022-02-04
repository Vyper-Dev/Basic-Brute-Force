import random
import time
from datetime import datetime


now1 = datetime.now()
dt_string1 = now1.strftime("%H:%M:%S")
print("date and time =", dt_string1)


File = "ThreeCharDict.txt"
f = open(File, 'w')


Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "?", "!", "&", "@", "*", "^", "%"]
Letterss = Letters
list(Letterss)
Dict = []
Try = True
Run = True
while Run == True:
        
        Letter = random.choice(Letterss)
        Letter2 = random.choice(Letterss)
        Letter3 = random.choice(Letterss)
        Add = [Letter, Letter2, Letter3]        
        Add1 = ''.join([str(element) for element in Add])
        exists = Dict.count(Add1)

        if exists == False:
                Dict.append(Add1)
                print("Added Item")

                if len(Dict) >= 328509:
                    for element in Dict:
                        f.write(element + "\n")
                    f.close()
                    now2 = datetime.now()
                    dt_string2 = now2.strftime("%H:%M:%S")
                    print("Start Time:", dt_string1)
                    print("End Time:", dt_string2)
                        
                        
                    Try = False
                    Run = False
                    break
