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

lives = 6

word_list = ["tent", "autobus", "insurance", "execute"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}')


display = []
for letter in chosen_word:
    display.append("_")
while "_" in display and lives > 0:
    guess = input("Guess a letter: ")
    found = False
    for index in range(len(chosen_word)):
        
        if chosen_word[index] == guess:
            display[index] = guess
            found = True
        
    if found == False:
        lives -= 1
        print(stages[lives])
            
    print(f"{' '.join(display)}")
if lives == 0:
    print("You lose!")
else:
    print("You win!")