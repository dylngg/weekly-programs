def main():
	# get input
	title = input('Enter the title of an article: ').lower()
	
	scale = clickbaitScale(title)
	if scale >= 6:
		# might be clickbait
		print('"', title, '" might be clickbait with a score of', scale)
	elif scale >= 8:
		# most likely clickbait
		print('"', title, '" is most likely is clickbait with a score of', scale)
	else:
		print('"', title, '" probably isn\'t clickbait with a score of', scale)
		
def clickbaitScale(title):
	possibility = 0
	
	# split title into words
	titleWords = title.split(' ')
	
	# regular clickbait words 
	regularClickbaitWords = [line.rstrip('\n') for line in open('regClickbaitWords.txt')]
	
	# most common clickbait words
	commonClickbaitWords = [line.rstrip('\n') for line in open('commonClickbaitWords.txt')]
	
	print(titleWords)
	
	for word in titleWords:
		# check for major clickbait words 
		if word in commonClickbaitWords:
			possibility += 3
		
		# check for regular clickbait words
		if word in regularClickbaitWords:
			possibility += 1
		
		# check for ?,! or #
		if '?' in word or '!' in word  or '#' in word :
			possibility += 4
		
		# check for all caps
		if word.isupper() is True:
			possibility += 6
			
		# check for ...
		if '...' in word:
			possibility += 3 
	
		# check for numbers
		if word .isdigit() is True:
			possibility += 2
	
		# other things for later: check for number of nouns vs verbs and adjectives, check for vauge things (the,this), check for number of nouns to adjectives (news tend to have more nouns than adjectives and verbs)

	return possibility
	
main()
