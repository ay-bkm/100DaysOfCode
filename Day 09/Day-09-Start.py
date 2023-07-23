programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}
#Retreiving items from directionary
print(programming_dictionary["Bug"])

#Adding new items to directionary

programming_dictionary["ALX"] = "This is my school"



#create empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}

#Edit an item in a dictionary
programming_dictionary["Bug"] = "Bug is an insect"
 
print(programming_dictionary)


#Loop through a dictionary
for key in programming_dictionary:

    print(programming_dictionary[key])