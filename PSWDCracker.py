import random
import time

Run = True
while Run == True:

	print("")
	print("Enter The Password:")
	password = input()
	Letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "?", "!", "$", "&", "@", "*", ".", " ", "(", ")", "/", ",", "-", ":", ";")
	list(password)
	Try = True
	I = 0
	
	if password == "quit":
			break
	
	while Try == True:
		
		number = password[I]
		Letter = random.choice(Letters)
		
		if Letter == number:
			print( )
			print(Letter)
			print("LETTER CORRECT \n")
			time.sleep(.0)
			I += 1
			if I >= len(password):
				print("Password Solved")
				print("Password: " + password)
				break
		
		else:
			print( )
			print(Letter)
			print("Attempting...\n")
