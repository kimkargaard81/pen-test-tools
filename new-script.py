#!/bin/python3

#Importing modules

import sys # Sys is System Functions and Parameters
from datetime import datetime as dt #importing a specific part of the datetime module with datetime dt

print(sys.version) #print the version of python being run
print(dt.now()) #print the current date and time

my_name = "Kim"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence"
print(sentence[:4]) #This takes the first word in the sentence, since it is four characters

print(sentence.split()) #This splits the sentence out into the individual words as a delimiter

sentence_split = sentence.split() #We can split a sentence 
sentence_join = ' '.join(sentence_split) #We can then join the sentence back together
print(sentence_join)

quote = "He said, 'give me all your money'" #This gives us quotes within a string (character escaping)
quote_1 = "They said, \"the world is round.\""  # This is another way of doing character escaping
print(quote)
print(quote_1)

too_much_space = "               hello      "
print(too_much_space.strip()) # Strips out the space around the string

print("A" in "Apple") #This will look for an A in Apple. But, this is case sensitive, so if the "a" was lowercase, we would get a flase

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #This is improved as we then don't have to worry about case sensitivity

movie = "The Hangover"
print("My favourite movie is {}.".format(movie)) #This allows us to us {} as a placeholder for the string

#Dictionaries - Key/Value pairs {}

drink = {"Sprite": 4, "Juice": 3, "Coke": 5, "Mountain Dew": 6} #This is what a dictionary looks like Note: The drink is the key and the price is the value
print(drink)

employees = {"Finance": ["Angela", "Kevin", "Oscar"], "IT": ["Ryan"], "Sales": ["Jim", "Dwight", "Pam", "Michael"]}
print(employees)

employees['HR'] = ["Toby"] #Add a new key/value pair
print(employees)

employees.update({"Support": ["Kelly", "Ryan"]}) #This will update a key/value pair, but remember that if you want to update an existing key/value pair that you need to include all the original key/value pairs unless you want them all removed and the new one to replace.
print(employees)

employees.update({"Sales": ["Jim", "Dwight", "Pam", "Ryan"]}) #This will add new key/value pairs to the dictionary
print(employees)

drink['Sprite'] = 6 # This will update the value of the key 
print(drink)

print(drink.get("Coke")) # This will get the value of the key 


#NB! Very worth knowing: Lists have (), Tuples use [] and Dictionaries use {} TAKE NOTE!!!!


sys.exit #Exits python cleanly


