#Hangman Game
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


end_of_game = False
word_list = [
'abruptly', 'absurd', 'abyss', 'avenue', 'awkward', 'beekeeper', 'bikini', 'blitz', 'blizzard' 'boggle', 'bookworm', 'boxcar', 'cobweb', 'cockiness', 'croquet', 'crypt', 
'curacao', 'cycle', 'daiquiri', 'dirndl',  'dwarves', 'embezzle', 'exodus', 'faking', 'fishhook', 'fixable', 
'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 
'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jelly', 'jigsaw', 'joking', 'jovial', 'jukebox', 'jumbo',  'kazoo', 'kiwifruit', 
'lengths', 'lucky', 'luxury',  'matrix', 'megahertz', 'microwave', 'nightclub', 'nowadays', 'ovary', 'oxidize', 'oxygen', 
'phlegm', 'pixel', 'quiz', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'subway', 'swivel', 'syndrome', 
'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'unknown', 'unworthy', 'unzip', 
'uptown', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 
 ]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
print(logo)
#Testing code

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
print(f'Pssst, the solution is {chosen_word}.')
