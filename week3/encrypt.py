
class DictionaryEncryption(object):

	def __init__(self):
		# read dictionary
		dictionaryFile = open("popular.txt",'r')
		lines = dictionaryFile.readlines()
		dictionaryFile.close()

		# add to list
		self.dictionary = []
		for line in lines:
			self.dictionary.append(line.strip('\n').replace('\\n', '').lower())
		
		self._input = ''
		self._key = []
		self._message = ''

	def decode(self, key):
		self._key = key
		message = ''
		
		# find message
		keys = key.split('-')
		for key in range(0,len(keys)):
			 message = message + ' ' + str(self.dictionary[int(keys[key])])
			
		return message

	def encode(self, input):
		self._input = input
		self._key = DictionaryEncryption.createKey(self, self._input) 
		
		return self._key  
	
	def formatKey(self, key):
		finalKey = ''
		for num in range(0,len(key)):
			if finalKey is not '':
				finalKey = finalKey + '-' + str(key[num])
			
			else:
				finalKey = str(key[num])
				
		return finalKey
	
	def createKey(self, input):
		
		# if numbers or just spaces
		if input.isdigit() is True or input.isspace() is True:
			raise Exception('Input needs to only have alphabet characters!')
			
		# if contains alphabet
		else:
			words = []
			key = []
			for letter in range(0,len(input)):
				words = input.split(' ')
		
			for englishWords in range(0, len(words)):
				try:
					key.append(self.dictionary.index(words[englishWords].lower()))
				except (ValueError,IndexError):
					raise ValueError(words[englishWords], 'was not found in dictionary. Try Again with all the words being in the english dictionary.')

		return DictionaryEncryption.formatKey(self, key)
