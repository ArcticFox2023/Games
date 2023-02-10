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
                   |___/    
'''

word_list = [
    'almond',
    'apple',
    'apricot',
    'asparagus',
    'avocado',
    'banana',
    'bean',
    'beef',
    'bread',
    'broccoli',
    'butter',
    'cake',
    'cantaloupe',
    'carrot',
    'cauliflower',
    'celery',
    'cereal',
    'cheese',
    'cherry',
    'chicken',
    'chickpea',
    'chip',
    'chocolate',
    'cocoa',
    'coconut',
    'cookie',
    'cream',
    'eggplant',
    'flour',
    'garlic',
    'grape',
    'kiwi',
    'lamb',
    'lemon',
    'lettuce',
    'lime',
    'mango',
    'milk',
    'mushroom',
    'onion',
    'orange',
    'papaya',
    'peach',
    'peanut',
    'peas',
    'pie',
    'pineapple',
    'plum',
    'pork',
    'potato',
    'pudding',
    'pumpkin',
    'blackberry',
    'rice',
    'roll',
    'salmon',
    'soup',
    'spinach',
    'tea',
    'toast',
    'trout',
    'walnut',
    'watermelon',
    'wheat',
    'yogurt',
    'zucchini'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
    'bunny'
]
lives = 6
print(stages[lives])
print(logo)
import random
def pick_word():
    word = random.choice(word_list)
    return word
word = pick_word()
word = list(word)
count = len(word)
guessed = ['_']*count
print(guessed)

def replace(word, new_guess, guess_result):
    # go over word find the new_guess spot
    for i in range(len(word)):
        if new_guess == word[i]:
            guess_result[i] = word[i]
    return guess_result

while True:
    answer = input("What would you like to guess: ")
    if answer not in word:
        print("That is incorrect")
        lives -= 1
        if lives == 0:
            print(word)
            print("Game over")
            break
        print(stages[lives])
        
    else:
        print("That letter is in the word")
        guessed = replace(word, answer, guessed)
        print(guessed)
        print(stages[lives])
        if guessed == word:
            print("You win!")
            break

            
        
