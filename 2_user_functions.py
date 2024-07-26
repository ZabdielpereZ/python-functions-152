# user defined functions!!!!!!

# They give us repeatable power

# print('='*50)

# syntax
# def function_name(parameters):
#     code block to be executed on function call

# Simple function

def divi():
    print('='*50)

# def divi(): # this is an example of returning a value to use later
#     return '='*50

# this = divi()
# print(this)

def greeting():
    print("Hello there traveler!!")

greeting()
greeting()
greeting()

#-- Function with parameters

# establish a required variable/value for our function

def personal_greeting(name):
    if isinstance(name, str):
        print(f"Hello {name}, welcome to user defined functions!!")
    elif isinstance(name, int):
        print("This function is meant to be a greeting, please enter a real name.")

personal_greeting("Zabdiel")
personal_greeting("James")
personal_greeting(1234567890) # the function as it's defined is expecting to be given a value when it's called
person = 'Eric'
personal_greeting(person)

def get_username():
    user_input = input("What's your username? ")
    return user_input
    
# player1 = get_username()
# print(f"Player 1's username is: {player1}")
# player2 = get_username()

# This function accepts no parameters, and we ask for user input inside of the function, this will only occur when the function is called
def whats_ur_name():
    thing = input("What's your name traveler? ")
    print(f"Let's welcome {thing}, the mysterious adventurer!!")

# this function requires a parameter, instead of asking the user for that data inside of the function, we're expecting it to be given to the function
def whats_ur_name2(thing):
    print(f"Let's welcome {thing}, the mysterious adventurer!")

# name = input("What's your name good sir? ")
# whats_ur_name2(name) 

# whats_ur_name()
# print(what's_ur_name()) # our print statement prints none to the screen because I haven't specified for my function to return anything, and so by default it returns a none value

divi()

def greet(anything):
    print(f"hello, {anything}")

greet("Jasmine")
greet("James")

divi()

#---- more complex example

def class_info(instructor, students):
    print(f"This class is taught by {instructor}!")
    class_size = len(students)
    print(f"It has {class_size} students")
    for student in students:
        print(student)

students_152 = ["Gamel", "Jeremaine", "Jasmine", "Vincent", "Eric", "Brian", "Liz", "Tyler"]
class_info("Travis", students_152)

divi()

class_info(students_152, "Travis")

divi()
students_153 = ["Sarah", "James", "John"]
class_info("Me", students_153)

divi()

def book_info(author, title):
    print(f"this author is: {author}")
    print(f"the title is: {title}")

    book_info("Neil Gieman", "Smoke and Mirrors")