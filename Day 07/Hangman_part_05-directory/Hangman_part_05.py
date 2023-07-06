import random
import art
import word_list

lives = 6

print(art.logo)

chosen_word = random.choice(word_list.word_list)
print(f'Pssst, the solution is {chosen_word}')


display = []
for letter in chosen_word:
    display.append("_")
    
while "_" in display and lives > 0:
    guess = input("Guess a letter: ")
    found = False
    if guess in display:
            print(f"You've already guessed the letter {guess}")
    for index in range(len(chosen_word)):
        
        if chosen_word[index] == guess:
            display[index] = guess
            found = True
        
        
    if guess not in chosen_word:
             print(f"{guess} don't exist in the word.")    
    if found == False:
        lives -= 1
        print(art.stages[lives])
    
            
    print(f"{' '.join(display)}")
if lives == 0:
    print("You lose!")
else:
    print("You win!")