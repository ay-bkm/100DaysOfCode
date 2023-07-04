import random

word_list = ["tent", "autobus", "insurance", "execute"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}')


display = []
for letter in chosen_word:
    display.append("_")
while "_" in display:
    guess = input("Guess a letter: ")
    for index in range(len(chosen_word)):
        
        if chosen_word[index] == guess:
            display[index] = guess
    print(display) 

