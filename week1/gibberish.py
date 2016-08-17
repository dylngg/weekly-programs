import string
import random

alphabet = list(string.ascii_lowercase)
weirdChar = ['!','@','#','$','%','^','&','*','(',')']
gibberish = ''

length = int(input('Enter length of gibberish: '))

for x in range(0,length):
	
	if random.randint(0,2) is 1:
		# alphabet
		gibberish += str(alphabet[random.randint(0,25)])
		
	elif random.randint(0,3) is 2:
		#number
		gibberish += str(random.randint(0,9) - 1)
		
	else:
		# weird character
		gibberish += str(weirdChar[random.randint(0,9) - 1])

print(gibberish)
