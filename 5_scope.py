def div():
    print('='*50)


# in python we have two diffrent types of scope. Global scope and local scope

# the scope determines what variable are accesible 

# Global scope is anywhere outside of a function or a for loop 

# Global Variable 
x =7 # Variabels defined on a global scope can be accsessed from anywhere in our code 
a = "words"
alist = ["item1", "item2", "item3"]

if x: 
    print(x)

# Local scopes is crated inside of a function (or a for loop)

def local_func():
    y = 10 # local variable only accesible inside of this function

print(x)

local_func()
    # print(y) # this will throw an error because y is not defined in this scope
 
books = [] # defined in a global scope. This library of books can be accessed anywhere in this file 

def add_to_library(author, title):
    book = [author, title] # defined on a local scope and only available inside of this function 
    books.append(book)

add_to_library("J.K. Rowling", "Harry Potter and the Deathly Hallows")
add_to_library("Neil Geiman", "Smoke and Mirrors")

def display_books():
    for book in books:
        div()
        print(f"title: {book[1]}")
        print(f"Author: {book[0]}")
        div()
    
display_books()