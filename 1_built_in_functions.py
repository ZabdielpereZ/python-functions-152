# Built in fuctions 

# Print() : Prints data to the sceen so it is visible to the user 
print('string1', 'string2', sep='==========')

# \n: new line character 
print("string1\n\n\n")
print("we're here now")

# \t: tab special character
print("this is\t\t", 'separated')

# \\: backlash characters adds a backlash 
print("this string should now have a backlash\\")

# string concatenation (adding multiple strings together to make a single string)
words = "add"
print("we can" + words + "strings together")

# Fortmatted string
name = 'alice'
age = 30

# using .format() method
print("name: {}, age: {}".format(name, age))

# Modern formatted string 
print(f"name: {name},\nAge: {age}")

#------------#

# input() : used to take user input
name = input("What is your name? ")
print(f"Hello, {name}!!")

# type() : can be used to return the data type of data in a variable
num = 10
print(type(num))

# isinstance(variable, type) : checks to see if variable holds a specific data type, always returns a boolean value (True or False)
num = 10
print(isinstance(num, int))

# len() : returns the length of an iterable object 
message = "Hello"
print(len(message))

#abs() : returns the absolute value of a number
number = -5
print(abs(number))

# round() : rounds a number to the nearest integer or specified number of decimal places
# must be a decimal above .5, for ex 4.51, in oder to round up

number = 4.567
print(round(number)) #output: 5
print(round(number, 2))#output: 4.57

print(round(4.5)) # output: 4
print(round(4.51))# output: 5

#sum() : returns the sum of all items in an iterable 
numbers = [1, 2, 3, 4]
print(sum(numbers))

# min() : returns the smallest value of an iterable
print(min(numbers))

# max() : returns the largest value in an iterable
print(max(numbers))

# pow(<num>, <to the power of>) : returns the power of a number
print(pow(2, 3)) # output: 8

#divmod(<num1>, <num2>) : returns a tuple containing the quotient and remainder of division
print(divmod(10, 3)) 

#-------------#

# int() : converts a value to an integer
print(int("10")) # output: 10
# print('10' + 5) error: can only concatenate str (not "int") to str

# str() : converts a value to a string
print(str(10), type(str(10)))# output: '10'

# float() : converts a value to a floating point number
print(float("10.5"), type(float("10.5"))) # output: 10.5

# bool() : converts a value to a boolean (True or False)
print(bool(0)) # output: False
print(bool(1)) # output: True
print(bool([])) # output: False
print(bool("")) # output: False
print(bool(-1)) # output: False 
print(bool(-81)) # output: False


names = []
print(bool(names)) # output: False
print(len(names)) # output: 0


# if-else statement
if names:
    print("hey look, there are name in here!")
else:
    print("Uh oh, no names in here yet")
