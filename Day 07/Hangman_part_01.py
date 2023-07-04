import random
word_list = ["sweater", "vexillology", "goverment"]

chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()
for char in chosen_word:
    if guess == char:
        print("right")
    else:
        print("false")