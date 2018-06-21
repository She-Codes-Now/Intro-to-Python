#Hands On After Functions Module

# 1. Write a function to print “Hello World”.
def say_hello_world():
	print("Hello World!)
#------------------------------------------------------------------------------


# 2. Write a function to add two numbers.
def add_two_numbers(a, b):
  c = a + b;
  return c;
  
sum1 = add_two_numbers(10, 20)
print(sum1)
#------------------------------------------------------------------------------




#Hands On At the End of the workshop

#Print Hello World.
print("Hello World!")
#------------------------------------------------------------------------------


#Take an input and print it.
name = input("What is your name?")
print(name)
#------------------------------------------------------------------------------


#Write a function to print your favorite game. Along with a message.
def my_favorite_game(game):
  if game.lower() == 'overwatch':
    print('I like overwatch!')
  elif game.lower() == ‘final fantasy':
    print('I like final fantasy!')
  else:
    print('I like ', game)

my_favorite_game(‘Overwatch')
#------------------------------------------------------------------------------


#Write a function to find if a number (e.g. n) is even or odd. 
#------------------------------------------------------------------------------
# Function Declaration
def isEvenOrOdd(n):
	if (n % 2 == 0):
		return 'Even'
	else:
		return 'Odd'

		
#Write a function to add two numbers.
# <answered above>
#------------------------------------------------------------------------------

#Given a list of favourite food: favorite_food = ["pizza", "ice cream", "green salad"]
#Print the list items using "for" loop
favorite_food = ["pizza", "ice cream", "salad"]

for food in favorite_food:
	print(food)
#------------------------------------------------------------------------------

#Print numbers from 1 to 10 using while loop.
i = 1

while i <= 10:
	print(i)
	i = i + 1
#------------------------------------------------------------------------------

#Shuffle a list
from random import shuffle

a = [1, 2, 3]
print("Original List: ", a)

shuffle(a)
print("Shuffled List: ", a)
#------------------------------------------------------------------------------


#Create a Person class. Create two objects - person1, person2 and display those.
class Person:
    '''An example of a class definition'''

    def __init__(self, name, height):  # method
        self.name = name	# variable (or state)
        self.height = height # variable (or state)

    def display(self):  # method
        print('(Name=%s, Height=%s)' %(self.name, self.height))

    def eat(self):  # method
        pass

    def sleep(self):  # method
        pass


# Refer to Person class definition on previous slide

# Create objects
person1 = Person("John", "5.7") # person1 is an object
person2 = Person("Jane", "5.7") # person2 is an object

# Call the methods
person1.display() 
person2.display()

#------------------------------------------------------------------------------

#Write an example code to demonstrate Exception Handling in Python
#Example 1
while True:
    try:
        x = int(input("Please enter a number: "))
        print(x)
    except ValueError:
        print("Oops!  That’s not a valid number.  Try again...")
        break

#Example 2
a = 10
b = 0
try:
	c = a/b
	print(c)
except ZeroDivisionError as err:
	print("Exception!: ", err)

#------------------------------------------------------------------------------