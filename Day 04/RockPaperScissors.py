import random
choice = int(input("Make your choice, 0 for Rock, 1 for Paper, 2 for Scissors"))
list = ["Rock","Paper","Scissors"]
computer_choice = random.randint(0,2)

if choice >= 3:
    print("You lost because you typed an invalid number!")
elif choice == 0 and computer_choice == 2:
    print(f"You chose: {list[choice]}\nCompute chose: {list[computer_choice]}")
    print("You Won!")
elif choice == 1 and computer_choice == 0:
    print(f"You chose: {list[choice]}\nCompute chose: {list[computer_choice]}")
    print("You Won!")
elif choice == 2 and computer_choice == 1:
    print(f"You chose: {list[choice]}\nCompute chose: {list[computer_choice]}")
    print("You Won!")
elif choice == computer_choice:
    print(f"You chose: {list[choice]}\nCompute chose: {list[computer_choice]}")
    print("it's a draw!")
else:
    print(f"You chose: {list[choice]}\nCompute chose: {list[computer_choice]}")
    print("You lost!")
