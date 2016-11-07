import math

def main(args):
	
	# get number to test
	possiblePrimeNum = int(input('Enter the number you want to test: '))
	
	yesNo = ' '
	outcome = isPrime(possiblePrimeNum)
	if outcome is not True:
		yesNo = ' not '

	print(str(outcome) + '! It seems like ' + str(possiblePrimeNum) + ' is' + yesNo + 'a prime number!')

# returns True/False if num is prime
def isPrime(num):
		
	# num less than two is not prime
	if num < 2:
		return False

	# if number is divisible by any num up to sqrt of num
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	
	# everything looks good!
	return True

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
