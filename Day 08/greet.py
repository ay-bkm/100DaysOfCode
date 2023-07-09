#Posional argument
def greet(name, age, language):
    print("#Posional argument")
    print(f"Hello I am {name}, {age} years old.\n")
    print(f"I am learning {language}.\n")
    print("And I am already in love with the language!")
greet("Ayoub", 26, "Python")
#Keyword argument
def greet(name, age, language):
    print("#Keyword argument")
    print(f"Hello I am {name}, {age} years old.\n")
    print(f"I am learning {language}.\n")
    print("And I am already in love with the language!")
greet(name="Ayoub", age=26, language="Python")
