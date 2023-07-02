#Not allowed to use max() or min()

scores = input("Write the scores.\n")
listOfScores = scores.split(" ")
heighest_score = int(0)
for score in listOfScores:
    if int(score) > heighest_score:
        heighest_score = int(score)
print(f"The heighest score: {heighest_score}")