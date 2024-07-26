# the goal of many functions is to produce something

#-- take something in as an argument
#-- manipulate it/do something to/with it
#-- return the output

name = "Travis"

data = type(name) # value is returned but not printed to the screen, so we dont get to see it
print(data)

print(type(name)) # print() is allowing us to see/view the returned data from the function 

# simple function with a return statement

def addition (a,b):
    return a + b

# def addition1(a,b): # this will do exactly the same thing, but above is easier to write 
# ans = a + b
# return ans

total = addition(5, 5)
print(total)

# this also works
print(addition(10, 10))

addition(1, 20) # here nothing prints to the screen because data is returned, but we're not doing anything with it 
print(addition(25, 25)) # here we're doing something with this data, printing it 

# doubler function that takes in a list of numbers and doubles each value in the list, then returns the new list

def doubler(nums):
    doubled_nums = []
    for num in nums:
        doubled_nums = num * 2
    doubled_nums.append(doubled_nums)
    return doubled_nums
# print (double_nums) # this won't execute because it is coming after our return statement. A return statement signifies the end of a function 

my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dnums = doubler(my_nums)
print(dnums)

#-- a function with no return 

def greeting_card(name): # a function without a return statement by default returns a none value
    print(f"Have a great day, {name}!")

card_message = greeting_card("Travis")

print(card_message)