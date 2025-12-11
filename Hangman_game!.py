import random

hangman = ['''
  ----
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|l  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|l  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|l  |
 / l  |
      |
=========''']

words = [
    'lion', 'tiger', 'cat', 'dog', 'elephant', 'giraffe',
    'zebra', 'bear', 'wolf', 'fox', 'rabbit', 'horse',
    'monkey', 'panda', 'kangaroo', 'camel', 'sheep',
    'goat', 'cow', 'deer', 'snake', 'eagle', 'shark',
    'dolphin', 'whale', 'penguin'
]
random_word = random.choice(words)
display = ['_'] * len(random_word) 
print(' '.join(display))

print('''
******** Welcome to Hangman game! 'Animals' ********
''')

lives = 6
guess_letter = []
print(hangman[0])

while '_' in display and lives > 0:
    guess = input('Please guess a letter or letters: ').lower()
    if guess in guess_letter:
      print('You already guessed that.Try again')
      print(f'You have {lives} more tries')
      continue

    guess_letter.append(guess)
    if guess not in random_word:
         lives -= 1
         print(hangman[6-lives])
    else:
      for position in range(len(random_word)):
          if random_word[position] == guess:
             display[position] = guess

    print(' '.join(display)) 
    print(f'You have {lives} more tries')

if lives == 0:
  print(hangman[-1])
  print(f'''
  *********
  You lose!
  *********
  Sorry the word is {random_word}
  ''')
else :
  print('''
  *********
  You win😁
  *********
  ''')