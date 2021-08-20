#!/bin/python3

# Variables and methods
quote = "All is fair in love and war." # A variable is basically a placeholder, which in this case is a string
print(quote.upper()) #added a method to make the quote uppercase
print(quote.lower()) # added a method to make the quote lowercase
print(quote.title()) # added a method to make the quote title case

print(len(quote)) # a method to count the length of the string

name = "Kim" #string
age = 40 # an integer int(30) note that an integer does not round, it just takes the value before the decimal
gpa = 4.1 # float (a float has a decimal point) float(4.1)

print(int(age))
print(int(30.1))

print("My name is " + name + " and I am " + str(age) + " years old.") # we can add strings and integers together.

age += 1 # we use the += to change the variable to something else
print(age) #printing out the new varible, since we changed it

birthday = 1
age += birthday
print(age)

print("My name is " + name + ", I am " + str(age) + " years old " + " and I graduated with a " + str(gpa) + " from Herlufsholm.")

print(int(age) + float(gpa))

print('\n')
#Functions
print("Here is an example of a function:")

#The below is considered a mini program and we have defined where we have defined our variables and an action to take
def who_am_i(): # This is a function and note that it is important to indent.
	name = "Kim" # a variable
	age = 40 # another variable, but worth noting that this is only stored as this value within the function and if we just print age again, it will use the earlier variable in the script
	print("My name is " + name + " and I am " + str(age) + " years old.") #This is the action to take
	
	
who_am_i()	# the actual function

# adding parameters
def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

#multiple parameters

def add(x,y):
	print(x + y)
	
add(7,7)

# From the above, it should be clear that we are building mini programs and we can have no parameters, single parameters or multiple parameters, depening on what we need.

def multiply(x,y):
	return x * y # a return stores the value for later, it does not print it to the screen
	
multiply(7,7)

def square_root(x):
	print(x ** .5) # this is the square root of whatever value gets defined.
	
square_root(64)

def nl():
	print('\n') # We can use this function to call a new line throughout the rest of the program using nl()
nl()


#Boolean expressions (True or False) When you think Boolean expressions, thing true or false

print("Boolean expressions")

bool1 = True #this is true
bool2 = 3 * 3 == 9 #this is true
bool3 = False #this is false
bool4 = 3 * 3 != 9 #this is false

print(bool1,bool2,bool3,bool4)
print(type(bool1))

nl()
#Relational and Boolean operators these are important to understand and to be able to use. Worth checking out the Truth Table for python on google (And, Or, XOR). 
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) # True
test_and2 = (7 > 5) and (5 > 7) # False
test_or = (7 > 5) or (5 < 7) # True
test_or2 = (7 > 5) or (5 > 7) # True for or, both have to be false to get false

test_not = not True #False
print(test_and,test_or2,test_not)

nl()
#Conditional Statements basically IF statements
nl()
def drink(money):
	if money >= 2:
		return "You've got yourself a drink!" 
	else:
		return "No drink for you"

print(drink(3))
print(drink(1))

# Multiple conditions in a conditional statement
nl()
def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "You are getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money!"
	elif (age <= 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too poor and too young"
		
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))
print(alcohol(20,6))


nl()

#Lists, a group of elements and everything in a list is called an item must have square brackets []
movies = ["Lethal Weapon 1", "Batman Begins", "The Dark Knight", "Moneyballs" ]

print(movies[1]) #This will return the second item in the list, as it starts counting from zero
print(movies[0]) # This returns the first item in the list
print(movies[1:3]) #This stops before item 3 on the list
print(movies[0:]) # this returns the entire list from the first item in the list
print(movies[1:]) # This returns the entire list from the second item in the list
print(movies[:1]) # This grabs before item one in the list, so item zero in the list only
print(movies[:3]) # this grabs te first three items in the list, stops before item four, but remember that it all starts counting with item zero
print(movies[-1]) # This will grab the last item in the list


print(len(movies)) # gives the number of items in the list
movies.append("The Dark Knight Returns") #When we want to append to the end of a list, we can use this function
print(movies)

movies.pop() #When we want to remove the last item in a list, we can use pop
print(movies)

movies.pop(0) #This will remove the first item in the list. 
print(movies)

movies.pop(1) #This will remove the second item in the list
print(movies)

movies.insert(0, "Lethal Weapon 2") #This will add an item to the top of the list
print(movies)

movies.insert(1, "The Dark Knight Rises") #This will add an item as the second item on the list
print(movies)

nl()

#Tuples - Do not change at all, ()

grades = ("a", "b", "c", "d", "e", "f") #This can not be changed as it is a tuple, not a list
print(grades[1])

nl()

#Looping 

#For Loops - start to finish of an interate
vegetables = ["tomato", "paprika", "cucumber", "carrot"]
for x in vegetables:
	print(x)

#While loops - Execute as long as true

i = 1

while i < 10: #if i is less than 10, then you need to do the following
	print(i)
	i += 1 # this will add one to i and then check if it is less than 10 and if so, do the same again (print i)
	

nl()






