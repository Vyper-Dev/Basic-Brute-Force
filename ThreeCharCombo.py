import random
from datetime import datetime

dt_string1 = datetime.now().strftime("%H:%M:%S")
print(f"Date and time: {dt_string1}")
f = open("ThreeCharDict.txt", 'w')
Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "?", "!", "&", "@", "*", "^", "%"]
Dict = []

while True:
    Letter1 = random.choice(Letters)
    Letter2 = random.choice(Letters)
    Letter3 = random.choice(Letters)
    Add1 = [Letter1, Letter2, Letter3]        
    Add2 = ''.join([str(element) for element in Add1])
    exists = Dict.count(Add2)

    if exists == False:
            Dict.append(Add2)
            if len(Dict) >= 328509:
                for element in Dict:
                    f.write(element + "\n")
                f.close()
                dt_string2 = datetime.now().strftime("%H:%M:%S")
                print(f"Start Time: {dt_string1} \nEnd Time: {dt_string2}")
                break