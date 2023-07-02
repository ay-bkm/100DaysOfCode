#Not allowed to use len() or sum()
students_heights = input("Write students heights seperated by space!\n")
listOfStudents = students_heights.split(" ")
totalHeight = 0

for height in listOfStudents:
    totalHeight = totalHeight + int(height)
print(f"The total height is: {totalHeight}")

students = 0
for student in listOfStudents:
    students += 1
print(f"Number of students is: {students}")


print (f"The average height (rounded) is: {round(totalHeight / students)}")

