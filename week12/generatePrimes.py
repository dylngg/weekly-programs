import math

def main(args):
	
	# get number to test
	primeSize = int(input('Let\'s Generate some primes! Enter the size of the max number array: '))
	
	primes = generatePrimes(primeSize)
	print('\n' + str(primes))

def generatePrimes(size):
	# uses the sieve of eratosthenes algorithm!
	# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

	sieve = [True] * size
	sieve[0] = False # 0 and 1 are not prime numbers
	sieve[1] = False

	# loop trough list
	for i in range(2, int(math.sqrt(size)) + 1):
		pointer = i * 2
		
		while pointer < size:
			sieve[pointer] = False
			pointer += i

	primes = []

	# add to primes list
	for i in range(size):
		if sieve[i] == True:
			primes.append(i)

	return primes

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
