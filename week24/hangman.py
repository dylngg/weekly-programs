import random
import argparse

def main(args):
    parser = argparse.ArgumentParser(description='Play Hangman!')
    parser.add_argument('-w', '--words', help='Input for the working directory', required=False)
    args = parser.parse_args()
    
    num_of_words = 2
    if args.words:
        num_of_words = int(args.words)
    
    word_list = get_words(num_of_words)
    answer = ''.join(word_list)
    
    lives = 0
    guessed_letters = []
    guessed_words = []
    
    # generate standard blank word
    unknown_word_list = [' ' if ch is ' ' else '_' for ch in answer]
    unknown_word = ''.join(unknown_word_list)
    
    print(generate_hangman(lives))
    print(unknown_word)
    
    while lives < 7:
        # get input for letters
        guess = str(input('Enter your guess: '))
        guess.strip()
        print()
        
        # guess is a word
        if len(guess) > 1:
            guessed_words.append(guess)
            
            for item in guess.split(' '):
                # check if guess is in word
                if item in answer:
                    guess_index = answer.index(item)
                    end_guess_index = guess_index + len(item)
                    unknown_word_list[guess_index:end_guess_index] = item
                
                else:
                    lives += 1
            
        # guess is a letter
        else:
            if guess in guessed_letters:
                print('--You\'ve Already tried that.--')
                continue
                
            elif guess in answer:
                guessed_letters.append(guess)
                letter_indexes = find_letter(answer, guess)
                for index in letter_indexes:
                    unknown_word_list[index] = guess
            
            else:
                guessed_letters.append(guess)
                lives += 1
        
        print('Lives Left:', 7 - lives)
        print('Guessed Letters:\n' + str(guessed_letters) + '\n')
        print(generate_hangman(lives))
        
        
        unknown_word = generate_unkown_word(unknown_word_list)
        print(unknown_word)
        if unknown_word in answer:
            break
        
    
    
    print('Answer:', answer)


def generate_hangman(lives):
    '''
    ------
    |   |
    |   O
    |  /|\
    |   |
    |  / \
    |
    '''
    
    hangman = '------\n|   |\n|   '
    if lives >= 1:
        hangman += 'O\n'
    else:
        hangman += '\n'
    
    hangman += '|  '
    
    if lives == 2:
        hangman += ' |'
    if lives == 3:
        hangman += '/|'
    if lives >= 4:
        hangman += '/|\\\n'
    else:
        hangman += '\n'
    
    hangman += '|  '
    if lives >= 5:
        hangman += ' |\n'
    else:
        hangman += '\n'
    
    hangman += '|  '
    if lives == 6:
        hangman += '/'
    if lives >= 7:
        hangman += '/ \\\n'
    else:
        hangman += '\n'
    
    hangman += '|'
    
    return hangman


def generate_unkown_word(unknown_word_list):
    
    return ''.join(unknown_word_list)


def get_words(num_of_words):
    with open("popular.txt",'r') as words_file:   
        lines = words_file.readlines()
        possible_words = [word.strip() for word in lines]
    
    words_file.close()
    
    hangman_words = []
    for x in range(0, int(num_of_words)):
        word_list = list(possible_words[random.randint(0, len(possible_words))])
        if x != num_of_words - 1:
            word_list.append(' ')
        
        
        hangman_words += word_list

    return hangman_words


def find_letter(word, letter):
    letter = letter.strip()
    
    return [pos for pos, ch in enumerate(word) if ch is letter]


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
