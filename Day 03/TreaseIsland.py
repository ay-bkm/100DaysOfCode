print("Welcome to Treasure Island.\nYou mission is to find the treasure.")
direction = input("Choose to go right or left?").lower()

if direction == "left":
   swimOrWait = input("You are infront of a lake, Do you WAIT for the boat or SWIM?").lower()
   if swimOrWait == "wait":
      whichDoor = input("in front of you there are 3 doors: blue, red, yellow, choose wisely!").lower()
      if whichDoor == "yellow":
         print("YOU WON!")
      else:
         print("Game Over!")
   else:
      print("Game Over!")
else:
   print("Game Over!")