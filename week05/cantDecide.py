import random

# Get the options
choicesInput = input('Enter your choices: ')

choices = choicesInput.split(',')
favorites = choices

print('Here are your choices:', choices)

# Repeat until Decision has been made
while True:
	# If you have more than one option
	if len(favorites) > 1:
		#Get Input and put it in a list
		favoriteInput = input('\n\nWhich ones are your favorite? (enter numbers "all" for all of the choices): ').lower()
		favoritesIndex = favoriteInput.split(',')
		favoritesIndex.sort()
		
	else:
		print('Good. You can stop freaking out now... Enjoy: "',favorites[likeChoice],'"')
		break
	
	if 'all' in favoritesIndex:
		print('Well... Since you cannot decide... Heres a random choice: ')
		likeChoice = random.randint(0,len(favorites)) - 1
		
		print(favorites[likeChoice])
		likability = input('Like it? ')
		
		if 'y' in likability:
			print('Good. You can stop freaking out now... Enjoy: "',favorites[likeChoice],'"')
			break
			
		else:
			print('If you don\'t like it, I\'m going to remove it...')
			favorites.pop(likeChoice)
			print('Your choices are now: ', favorites)
	
	elif favoritesIndex is '':
		print('Uhh. You have to enter something.')
	
	else:
		newFavorites = []
		for x in range(0,len(favoritesIndex)):
			newFavorites.append(favorites[int(favoritesIndex[x]) - 1])
			
		favorites = newFavorites
		print('Your choices are: ', favorites)
	
