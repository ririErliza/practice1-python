


#-----------------------------------variables--------------------------------------

# name="Kiki"
# age=33
# name1="Lilia"
# HEIGHT=153
# my_name="Riri"
# _name="Ryan"

# for, if, while, import have specific meaning, therefore cant be used as variables names


#----------------------------------------------------------------------------------

#--------------------------expressions and statements------------------------------



#expression is any sortf of code that return a value

1+1  #this gonna return 2
"Kiki" #this gonna return string Kiki



#statement is operation on a value

name2="Rose"
#print(name2)

#above can be written like this too :  name2="Rose" ; print(name2)  2 statements in one single line separated by semicolon

#----------------------------------------------------------------------------------

#----------------------------------comment-----------------------------------------

#using hash mark (#) to comment a code. everything after the hash mark is ignored.

#---------------------------------indentation--------------------------------------

#indentation in python matters, has a meaning. 
# everything indented belongs to a block like a control statement or conditional block or function or a class body


#----------------------------------------------------------------------------------

#-------------------------------Data Types-----------------------------------------

#string
name3="Beau"

#checking data types method 1
#print(type(name3)) #will return <class 'str'> at the console

#checking data types method 2 (by comparing it)
#print(type(name3)== str) #will return True at the console

#or
#print(isinstance(name,str)) #will return True at the console



#number
amount1=2
#print(isinstance(amount1,int)) #will return True at the console
#print(isinstance(amount1,float)) #will return False
#print(isinstance(amount1,str)) #will return False

amount2=2.9
#print(isinstance(amount2,float)) #will return True

amount3=float(2)  #this here is converting the integer to float
#print(isinstance(amount3,float)) #will return True

amount4=int("20") #this here is converting the string to integer
#print(isinstance(amount4,str)) #will return False
#print(isinstance(amount4,int)) #will return True

#converting str to number vv (casting)
number="23"
# numberToInt = int(number)
# print(isinstance(numberToInt,int)) #will return True

number1="test"
#numberToInt1 = int(number1)
#print(isinstance(numberToInt1,int)) #will return error



#other data types

# complex for complex numbers
# bool for booleans
# list for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets



#----------------------------------------------------------------------------------


#-------------------------------OPERATORS------------------------------------------

# We've already seen one, that is assignment operator (=), 
# which is used to assign a value to a variable or to assign a variable value to another variable

#--------------Arithmetic Operators-----------------

1+1 #2
2-1 #1
2*2 #4
4/2 #2
4%3 #1
4**2 #16  #exponents, four to the power of two is 16
5//2 #2 #floor division, running down to the nearest integer

#plus sign can be used to concatenate too
# print("Scamp " + "is a good dog")

#plus equal
# age1=8
# age1+=8 # the same as age1 = age1 + 8 
# print(age1)

# age1*=3
# print(age1)


#--------------Comparison Operators-----------------
a=1
b=2

# print(a==b) #False
# print(a!=b) #True
# print(a>b) #False
# print(a<=b) #True



#--------------Boolean Operators--------------------

condition1=True
condition2=False

# print(not condition1) #False -- not means not true
# print(condition1 and condition2) #False -- and means both have to be true, if one of them is false then it will return false
# print(condition1 or condition2) #True -- or means either one needs to be true

#-----------------or------------------

# print(0 or 1) ## 1
# print(1 or 0) ## 1
# print(False or 'hey') ## hey
# print('hey' or False) ## hey
# print('hey' or True) ## hey
# print(True or 'hey') ## True
# print('hi' or 'hey') ## hi
# print('hey' or 'hi') ## hey
# print([] or False) ## False
# print([] or True) ## True
# print(False or []) ## []
# print(True or []) ## True

# print(True or False) ## True
# print(False or True) ## True

# print(False or 0) ## 0
# print(0 or False) ## False
# print(True or 0) ## True
# print(0 or True) ## True

#------------------------------------#

# True1 or True2 -- return True1
# True or False -- return True
# False or True -- return True
# False1 or False2 -- return False2

#------------------------------------#

#------------Falsies-----------------#

# Sequences and Collections:
# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ""
# Empty ranges range(0)

# Numbers:
# Zero of any numeric type.
# Integer: 0
# Float: 0.0
# Complex: 0j

# Constants:
# None
# False

#------------------------------------#

#----------------and------------------

# and only evaluates the second argument if the first one is true
# so if the first argument is falsy, it returns that argument --that falsy, 
# otherwise it evaluates the second argument and return the second argument (even if it's falsy)

# print(0 and 1) ## 0
#cprint(1 and 0) ## 0
#cprint(1 and 2) ## 2
# print(False and 'hey') ## False
# print('hi' and 'hey') ## hey
# print([] and False) ## []
# print(False and []) ## False




#--------------Bitwise Operators--------------------
#very rarely uses, only specific situation
# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation




#--------------is & in Operators--------------------

# is --> identity operator
# it's used to compare two objects and returns true if both are the same objects

#in --> membership operator
# this is used to tell if a value is contained in a list or another sequence




# #--------------Ternary Operator---------------------

# #to quickly define a conditional

# #slow way:
# def is_adult(age):
#     if age<18:
#         return True
#     else:
#         return False

# #ternary operator
# def is_adult2(age):
#     return True if age < 18 else False


# #----------------------------------------------------------------------------------

# #--------------------------------Strings-------------------------------------------

# "Beau"
# 'Beau'
# name= "Beau"
# # phrase=name+ " is my name"
# # name += " yes my name"

# #multiline string
# print("""Lili is

# 33

# years old
# """)



# #--------------String Methods---------------------
# #strings method dont alter the original, it will return a new modified string

# print(name.lower())
# print(name)

# print(len(name)) #the length of the string, this will print 4

# print("au" in name) #using in operator to check whether certain substring exist, this will print true

# # print("lili".upper())  #LILI
# # print("LiLi".lower()) #lili
# # print("LiLi the woman".title()) #Lili The Woman
# # print("LiLi".islower()) #False

# # isalpha() --> to check if a string contains only characters and is not empty
# # isalnum() --> to check if a string contains characters or digits and is not empty
# # isdecimal() --> to check if a string contains digits and is not empty
# # lower() --> to get a lowercase version of a string
# # islower() --> to check if a string is lowercase
# # upper() --> to get a uppercase version of a string
# # isupper() --> to check if a string is uppercase
# # title() --> to get a capitalized letter of a string
# # startswith() --> to check if the string starts with a specific substring
# # endswith() --> to check if the string ends with a specific substring
# # replace() --> to replace a part of a string
# # split() --> to split a string on a specific character separator
# # strip() --> to trim the whitespace from a string
# # join() --> to append new letters to a string
# # find() --> to find the position of a substring


# #--------------Escaping Characters----------------
# #escaping is a way to add special characters into a string --> putting a backslash (\) character

# print("Bea\"au") # Bea"au
# print('Bea"au') # Bea"au
# print('Be\nau') # Be        #putting the next after \n at a new line
#                 # au


# #--------------String Characters & Slicing--------
# #getting a specific character in a string

# # name= "Beau"

# print(name[1]) #get letter at index 1 -> e

# print(name[0]) #get letter at index 0 -> B

# print(name[-1]) #get letter at index -1 -> u  #it's from the backward but not startng from zero coz there is no negative zero

# print(name[1:2]) #get letter starting at index 1 and ending before index 2 --> e

# print(name[1:3]) # ea

# print(name[1:4]) # eau



# #----------------------------------------------------------------------------------
# #--------------------------------Booleans------------------------------------------
# done= True
# # done = False

# if done:
#     print("yes")
# else:
#     print("no")


# # number is always true, except zero 0
# # minus number, like -1 is true too
# # strings are always true, excet empty string ""

# #------checking-------

# print(type(done)==bool) #True

# #--------any----------

# book_1_read=True
# book_2_read=False

# # checking if any of them are True 
# read_any_book=any([book_1_read,book_2_read])

# # and then it's going to set this to True
# print(read_any_book) #True


# #--------all----------

# ingredients_purchased = True
# meal_cooked = False

# # this will return True only if all of the values are True
# ready_to_serve = all([ingredients_purchased, meal_cooked])

# print(ready_to_serve) #False


# #----------------------------------------------------------------------------------

# #--------------------------------Number Data Types---------------------------------

# # int, integer --> whole number
# # float --> any number with decimal point
# # complex number --> an extention of the familiar real number system 
# #                    in which all numbers are expressed as a sum of a real part and an imaginary part
# #                    imaginary numbers are real multiples of the imaginary unit which is the square root of negative one
# #                    often written i in mathematics or j in engineering
# #                    in python is written with a j suffix

# num1 = 2+3j
# print(num1.real, num1.imag) # 2.0 3.0

# num2 = complex(2,3)
# print(num2.real, num2.imag) # 2.0 3.0

# #----------------------------------------------------------------------------------

# #--------------------------------Built-in Functions--------------------------------

# # abs --> will return the absolute value of a number

# print(abs(5.5)) # 5.5

# print(abs(-5.5)) # 5.5

# #round --> round to the nearest integer

# print(round(5.5)) # 6
# print(round(5.4)) # 5

# #----------------------------------------------------------------------------------

# #--------------------------------Enums---------------------------------------------

# # enums are readable names that are bound to a constant value
# # to use enums we're going to import enums from the enum standard library module
# # the only way to create constants in python
# # we can use enum to create a constant and then it cant be reassign a value

# from enum import Enum

# class State(Enum):
#     INACTIVE = 0
#     ACTIVE = 1

# print(State.ACTIVE.value) # 1

# print(State['ACTIVE'].value) # 1

# print(State(1)) # State.ACTIVE

# print(State['ACTIVE']) # State.ACTIVE

# print(list(State)) # [<State.INACTIVE: 0>, <State.ACTIVE: 1>]

# print(len(State)) # 2
# #----------------------------------------------------------------------------------

# #--------------------------------User Input----------------------------------------

# # get user input by using input function

# # print("What is your age?")
# # age = input()
# # print("I see, Your age is " + age)

# # # can be written like this too

# # age2 = input("What is your age? ")
# # print("OK, Your age is " + age2)

# #----------------------------------------------------------------------------------

# #------------------------------Control Statements----------------------------------

# condition3 = True

# # if condition3 is True then it's going to run everything in the block

# if condition3 == True:
#     print("The condition")
#     print("was", condition3)

# print("outside if, this is outside the block")

# # elif, else if

# condition4=False
# name="Favio"

# if condition4 == True:
#     print("The condition")
#     print("was True")
# elif name=="Roger":
#     print("Hello Roger")
# elif name == "Syd":
#     print("Hello Syd")
# elif name == "Favio":
#     print("Hello Favio")





# #----------------------------------------------------------------------------------

# #--------------------------------------Lists---------------------------------------

# # Lists are an essential python data structure


# dogs = ["Rubble", "Chase", "Rocky"]

# something = ["Roger", 1, True, "Syd", 2, "Beau"]

# print(dogs[1]) # Chase

# print(dogs[-1]) # Rocky

# print(something[2:4]) # slice from index 2 til index 4 (index 4 not included)
# #                        [True, 'Syd']

# print(something[2:]) # slice from index 2 til the end of the list
# #                        [True, 'Syd', 2, 'Beau']

# print(something[:3]) # slice from beginning of the list til index 3
# #                        ['Roger', 1, True]


# #--------length of the list (more like how many items inside the list)----------

# print(len(dogs)) # 3

# print(len(something)) # 5



#----------using in operator-------

# print("Rocky" in dogs) # True

# print("is Beau in dogs list? it is ", "Beau" in dogs) # is Beau in dogs list? it is  False



#--------update item in the list-----

# dogs[2] = "Beau" #update item at index 2 from "Rocky" to "Beau" to the list
# print(dogs) # ['Rubble', 'Chase', 'Beau']



#--------adding item--------
# only work to add 1 item at a time

# dogs.append("Rocky")
# print(dogs) # ['Rubble', 'Chase', 'Beau', 'Rocky']



#--------combining list--------
# adding more than 1 item, use combining list

# dogs.extend(["Skye", "Liberty"])
# print(dogs) # ['Rubble', 'Chase', 'Beau', 'Rocky', 'Skye', 'Liberty']


# plus equal sign work the same as extend

# dogs += ["Trek", "Zuma"]
# print(dogs) # ['Rubble', 'Chase', 'Beau', 'Rocky', 'Skye', 'Liberty', 'Trek', 'Zuma']


#--------remove item from list--------

# dogs.remove("Trek")
# print(dogs) # ['Rubble', 'Chase', 'Beau', 'Rocky', 'Skye', 'Liberty', 'Zuma']

# pop remove 1 item, from the last 
# print(dogs.pop()) # Zuma
# print(dogs) # ['Rubble', 'Chase', 'Beau', 'Rocky', 'Skye', 'Liberty']



#------------inserting item to a list-----------

# list_numbers = [2,4,5,6,9]
# list_numbers.insert(1, 3) # insert 3 at the index 1
# print(list_numbers) # [2, 3, 4, 5, 6, 9]


# items = ["Roger","Syd", "Quincy", "Beau", "Marybelle"]
# items.insert(2,"test")
# print(items) # ['Roger', 'Syd', 'test', 'Quincy', 'Beau', 'Marybelle']

#------------slices-----------

# items[1:1] = ["Test1", "Test2"]
# print(items) #['Roger', 'Test1', 'Test2', 'Syd', 'test', 'Quincy', 'Beau', 'Marybelle']


#-------------Sorting Lists-------------------------

# items.sort()
# print(items) # ['Beau', 'Marybelle', 'Quincy', 'Roger', 'Syd', 'Test1', 'Test2', 'test']

#-----another example-----

items2 = ["Sri","budi", "Heri", "Agus", "Rafael", "Endah","rafael"]


# using global function sorted
# print(sorted(items2, key=str.lower)) # ['Agus', 'budi', 'Endah', 'Heri', 'Rafael', 'rafael', 'Sri']
# print(items2) # ['Sri', 'budi', 'Heri', 'Agus', 'Rafael', 'Endah', 'rafael']



# using function sort()
# items2.sort()
# print(items2) # ['Agus', 'Endah', 'Heri', 'Rafael', 'Sri', 'budi', 'rafael']



# # it will print the lowercase at the end of the list, solving it by adding key=str.lower
# items2.sort(key=str.lower)
# print(items2) #['Agus', 'budi', 'Endah', 'Heri', 'Rafael', 'rafael', 'Sri']



# # copy a list using items[:]
# itemscopy = items2[:]
# print(itemscopy) # ['Agus', 'budi', 'Endah', 'Heri', 'Rafael', 'rafael', 'Sri']  # karena diatas items2 udah disort jd hasil copyan jg versi sort nya




#----------------------------------------------------------------------------------

#--------------------------------Tuples--------------------------------------------

# Tuples are another fundamental python data structure
# Allow us to create immutable groups of objects
# Tuples are IMMUTABLE
# Once Tuple is created, it cant be modified
# CAnt add or remove items
# Tuples are created in a way similar to lists but using parentheses instead of square brackets

students = ("Rocky", "Rubble", "Zuma", "Liberty", "Everest")

# print(students[-1])  # Everest

# print(students.index("Rocky"))  # 0

# print(len(students))  # 5

# print("Everest" in students) # True

# print(sorted(students)) # ['Everest', 'Liberty', 'Rocky', 'Rubble', 'Zuma']

# newTuple = students + ("Skye", "Ryder")
# print(newTuple) # ('Rocky', 'Rubble', 'Zuma', 'Liberty', 'Everest', 'Skye', 'Ryder')

#----------------------------------------------------------------------------------

#--------------------------------Dictionaries--------------------------------------

# another important python data structure
# dictionaries allow us to create key value pairs
# curly braces is used in dictionaries {"key":"value"}
# the key can be any immutable value such as a string, a number, or a tuple
# the value can be anything we want
# dictionary can contain multiple key value pairs

# cat1 = { "name":"Sam", "age":4  }

# print(cat1["name"]) # Sam

# #----change the name----
# cat1["name"] = "Syd"
# print(cat1["name"]) # Syd

# #----GET method----
# print(cat1.get("color")) # None

# print(cat1.get("name")) # Syd

# print(cat1.get("color", "brown")) # brown  # if it cant find color in the dictionary it will return brown

# print(cat1)

# cat1 = { "name":"Sam", "age":4, "color":"green"  }

# print(cat1)

# print(cat1.get("color", "brown")) # green # if it can fin the color in the dictionary, it will return the color from dictionary

# #----POP method----
# print(cat1.pop("name")) # Sam  # POP will return the item we deleted from dictionary

# print(cat1) # {'age': 4, 'color': 'green'}

# #----POPITEm method----
# print(cat1.popitem()) # ('color', 'green')  # we pop the last item from dictionary

# print(cat1) # {'age': 4}

# #----checking if key is in dictionary------

# print("color" in cat1) # False

# #-----print keys and values----------

# cat2={ "name":"Gloria", "age":3, "color":"brown"  }
# print(cat2.keys()) # dict_keys(['name', 'age', 'color'])

# print(list(cat2.keys())) # ['name', 'age', 'color']

# print(cat2.values()) # dict_values(['Gloria', 3, 'brown'])

# print(list(cat2.values())) # ['Gloria', 3, 'brown']

# print(list(cat2.items())) # [('name', 'Gloria'), ('age', 3), ('color', 'brown')]

# print(len(cat2))  # 3, there are 3 items inside the dictionary

# #--adding new item in the dictionary--
# cat2["favorite food"] ="Meat"
# print(cat2)  # {'name': 'Gloria', 'age': 3, 'color': 'brown', 'favorite food': 'Meat'}

# #-----delete item----------
# del cat2["color"]
# print(cat2) # {'name': 'Gloria', 'age': 3, 'favorite food': 'Meat'}

# #-----copy dictionary----------
# cat2copy = cat2.copy()
# print(cat2copy) # {'name': 'Gloria', 'age': 3, 'favorite food': 'Meat'}

# #----------------------------------------------------------------------------------

# #--------------------------------Sets----------------------------------------------
# # another important python data structure
# # kind of work like Tuples but they're not ordered, kind of work like dictionaries but they dont have keys
# # Sets are MUTABLE, so we can change them
# # Frozen Set is the IMMUTABLE set

# set1 = {"Boo", "Foo", "Loo", "Roo"}
# set2 = {"Roo"}
# set3 = {"Noo"}

# intersect = set1 & set2
# print(intersect) # {'Roo'} set1 and set2 only have "Roo" that in common

# mod = set1 | set3
# print(mod) # {'Noo', 'Boo', 'Roo', 'Foo', 'Loo'} we get each item from both sets

# mod = set1 - set2
# print(mod) # {'Boo', 'Loo', 'Foo'} we get the differences between set1 and set2

# mod = set1 > set2
# print(mod) # is set1 greater than set2? # True

# print(list(set1)) # ['Roo', 'Loo', 'Foo', 'Boo']

#----------------------------------------------------------------------------------

#--------------------------------Functions-----------------------------------------

# function let us create a set of instructions that we can run when needed
# indentation matter. it can be 2 or 4 spaces. as long as it is indented the same exact amount

# def hello():
#     print("Hello!")

# hello() #Hello!
# hello() #Hello!

# def hi(name): # putting argument here
#     print("Hi! "+ name)

# hi("Diana") # Hi! Diana
# hi("Arissa") # Hi! Arissa
# # hi() # TypeError: hi() missing 1 required positional argument: 'name'  # because we didnt pass any name inside

# def yuhuu(name="the one who cant be name"): # putting an optional argument
#     print("Yo! " + name)

# yuhuu("Diana") # Yo! Diana
# yuhuu("Arissa") # Yo! Arissa
# yuhuu() # Yo! the one who cant be name

# def annyeong(name, age):
#     print("Annyeong! " + name + ", you are " + str(age) + "years old!")

# annyeong("Beau",39) # Annyeong! Beau, you are 39years old!

#----------------------------------------------------------------------------------

#--------------------------------Variable Scope------------------------------------

#----Global Variable----

# age=8  # this variable declared globally

# def test():
#     print(age)

# print(age)  # 8
# test()      # 8 


#----Local Variable----
# (only available inside the function)

# def test():
#     age= 9
#     print(age)


# test() # 9

# print(age) # NameError: name 'age' is not defined

#----------------------------------------------------------------------------------

#--------------------------------Nested Functions----------------------------------

# a function defined inside a function is visible only iniside that function
# this is useful to create utilities that are useful to create a function but not useful outside of it

# def talk(phrase): # we declare function talk and inside that function, we declare another function say
#     def say(word):
#         print(word)

#     words = phrase.split(' ')
#     for word in words:
#         say(word)

# talk('I am going to buy milk')
# # I
# # am
# # going
# # to
# # buy
# # milk

# def count():
#     count=0

#     def increment():
#         nonlocal count  # nonlocal. this allows us to access count variable that was declared outside increment() function but inside count() function
#         count += 1
#         print(count)
    
#     increment()

# count() # 1

# #----------------------------------------------------------------------------------

# #--------------------------------Closures------------------------------------------

# # if we return a nested function from a function that nested function has access to 
# # the variables defined in that function even if that function is not active anymore

# def counter():
#     count1=1

#     def increment():
#         nonlocal count1 
#         count1 += 1
#         return count1
    
#     return increment

# increment = counter()

# print(increment()) # 2
# print(increment()) # 3
# print(increment()) # 4
# print(increment()) # 5
# #----------------------------------------------------------------------------------

# #--------------------------------Objects-------------------------------------------

# # Everything in python is an object
# # even values of basic prim of types like integers, strings, floats, lists, tuples, dictionaries
# # objects have attributes and methods that can be accessed using dot syntax

# banana = 8

# print(banana.real) # 8
# print(banana.imag) # 0
# print(banana.bit_length()) # 4 # bit length method return the number of bits necessary to represent this number in binary notation

# grapes = [1,2]
# grapes.append(3)
# grapes.pop()
# print(grapes) # [1, 2]
# print(id(grapes)) # 2503032173888 # the id global function provided by python lets you inspect the location in memory for a particular object

# # some objects are mutable and some are immutable

# #----------------------------------------------------------------------------------

# #--------------------------------Loops---------------------------------------------

# # while loop --> will repeat the block until the condition is evaluated as false
# kondisi = True
# while kondisi == True:
#     print("Hello while loop")
#     kondisi= False

#     # Hello while loop
#     #------done after the iteration meet kondisi=False----- 

# hitung=0
# while hitung<10:
#     print("The condition is True")
#     hitung+=1
# print("After the loop")

# #------will be orinted like below----

# # The condition is True
# # The condition is True
# # The condition is True
# # The condition is True
# # The condition is True
# # The condition is True
# # The condition is True
# # The condition is True
# # The condition is True
# # The condition is True
# # After the loop


# # For loop --> using for loop we can tell python to execute a block for a predetermined amount of times up front and without the need 
# # of a separate variable and conditional to check its value
# # it is commonly used to iterate item in a list

# oranges = [1,2,3,4,5]

# for orange in oranges: # for each item in the list we're gonna print the item
#     print(orange)

# # 1
# # 2
# # 3
# # 4
# # 5

# # using range
# for item in range(5):
#     print(item)

# # 0
# # 1
# # 2
# # 3
# # 4

# print("-------------------------------")

# # enumerate
# apples = [1,2,3,4,5]
# for index, apple in enumerate(apples):
#     print(index, apple)

# # 0 1
# # 1 2
# # 2 3
# # 3 4
# # 4 5

# # (index and item are printed side by side)

# print("-------------------------------")

# members = ["Zuma", "Rocky", "Marshall"]
# for index, member in enumerate(members):
#     print(index, member)

# # 0 Zuma
# # 1 Rocky
# # 2 Marshall

# print("-------------------------------")


# #--------------------------------Break and Continue--------------------------------

# # both while and for loops can be interrupted inside the block using either break or continue
# # continue --> stops the current iteration and tells python to execute the next one
# # break --> stops the loop altogether and goes on with the next instruction after the loop ends

# kiwis = [1,2,3,4]
# for kiwi in kiwis:
#     if kiwi == 2:
#         continue
#     print(kiwi)


# # 1
# # 3
# # 4


# print("-------------break------------------")

# for kiwi in kiwis:
#     if kiwi == 2:
#         break
#     print(kiwi)

# # 1

# print("-------------------------------")

# #----------------------------------------------------------------------------------

# #--------------------------------Classes-------------------------------------------

# #

# class Wolf:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("awooooo")

# roger = Wolf("Roger",8)

# print(type(roger)) # <class '__main__.Wolf'>
# print(roger.name) # Roger
# print(roger.age) # 8

# roger.bark() # awooooo

# print("-------------------------------")


#---------INHERITANCE---------------
# class Animal:
#     def walk(self):
#         print("Walking....")

# class Tiger(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("haooooom")

# beau = Tiger("Beau", 7)

# print(beau.name)
# beau.bark()
# beau.walk() #Beau inherit this method from Animal class 

# Beau
# haooooom
# Walking....
print("-------------------------------")

#----------------------------------------------------------------------------------

#--------------------------------Modules-------------------------------------------

# every python file is a module, we can import a module from other files and that's the base of any program
# of moderate complexity as it promotes a sensible organization and code reuse so it's basically how we can 
# create a software that has multiple python programs in the same piecce of software
# in the typical python program, one file acts as the entry point and the other files are modules and exposed functions
# that we can call from other files

from dog import bark
bark()

# wooof!

print("-------------------------------")

from lib import dog2

dog2.bark()

# wooof woof 2!

print("------------another way-------------------")

from lib.dog2 import bark
bark()

# wooof woof 2!

print("------------another module----------------")

# There are a lot of modules available
# Here are some of them
# math for math utilities 
# re for regular expression 
# json to work with json
# datetime to work with dates
# sqlite3 to use SQLite
# os for Operating System utilities
# random for random number generation
# statistics for statistics utilities
# requests to perform HTTP Network requests
# http to create HTTP servers
# urllib to manage URLs


# Math module

import math
print(math.sqrt(4)) # 2.0

from math import sqrt
print(sqrt(16)) # 4.0

print("-------------------------------")

#----------------------------------------------------------------------------------

#--------------------------------Arguments from Command Line-----------------------

# Accepting Arguments
# $ python test.py --> type this at the terminal to run python (just another way other than pressing the run button)

#----------------------------------------------------------------------------------

#--------------------------------Lambda Functions----------------------------------

lambda num : num*2
#----------------------

multiply = lambda a,b : a*b
print(multiply(2,4))  # 8

# the utility of lambda function comes when combined with other python functionality
# for example in combination with map, filter, and reduce 

print("-------------------------------")

#----------------------------------------------------------------------------------

#--------------------------------Map, Filter, Reduce-------------------------------

# python provides three useful global functions that we can use to work with collections
# so this is map, filter, reduce


# ------MAP-------
numbers = [1,2,3]

# double = lambda a : a*2

# result = map(double, numbers)

result = map(lambda a : a*2, numbers) # the same as 2 lines above

print(list(result)) # [2, 4, 6]

print("-------------------------------")

#-----FILTER-----

numbers2 = [1,2,3,4,5,6]

# def isEven(n):
#     return n%2 == 0

# result=filter(isEven,numbers2)

result=filter(lambda n:n%2==0,numbers2)



print(list(result)) #[2, 4, 6]

print("-------------------------------")

#-----REDUCE-----

# long way, without using reduce

expenses = [
    ('Dinner', 80),
    ('Car Repair', 120)
]

sum=0
for expense in expenses:
    sum+=expense[1]

print(sum) # 200

print("-------------------------------")

# using reduce

from functools import reduce

expenses2 = [
    ('Dinner', 30),
    ('Car Repair', 20)
]

sum=reduce(lambda a,b:a[1]+b[1], expenses2)

print(sum) # 50


#----------------------------------------------------------------------------------

#--------------------------------Recursion-----------------------------------------

# A function in python can call itself, that's what recursion is
# It can be useful for e.g. factorial calculation

# 3! = 3*2*1=6
# 4! = 4*3*2*1=24
# 5! = 5*4*3*2*1=120

def factorial(n):
    if n==1:return 1            # base case
    return n*factorial(n-1)     # recursive case

print(factorial(3)) # 6

# we always need the base case so the recursion can stop

#----------------------------------------------------------------------------------

#--------------------------------Decorators----------------------------------------

# decorators in python are a way to change, enhance, or  alter in anyway how a function works
# decorators are defined with the at symbol followed by the decorator name just before the function definition

def logtime(func):
    def wrapper():
        #do something before
        print("before")
        val= func()
        # do something after
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("hello")

hello()

"""
before
hello
after

""" 

#----------------------------------------------------------------------------------

#--------------------------------Docstrings----------------------------------------

# work similar like comment, to tell what this code is going to do (giving information)
# writing docstring: put 3 quotation marks before and after strings

def increment(n):
    """Increment a number"""
    return n+1

print(increment(3)) # 4

print(help(increment))
"""
Help on function increment in module __main__:

increment(n)
    Increment a number

None
"""

#------------------------------------------------------------

class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name=name
        self.age=age

    def bark(self):
        """Let the dog bark"""
        print("WOF!")

print(help(Dog))
"""
Help on class Dog in module __main__:

class Dog(builtins.object)
 |  Dog(name, age)
 |
 |  A class representing a dog
 |
 |  Methods defined here:
 |
 |  __init__(self, name, age)
 |      Initialize a new dog
 |
 |  bark(self)
 |      Let the dog bark
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

None
"""

#----------------------------------------------------------------------------------

#--------------------------------Annotations---------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Exceptions----------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------With----------------------------------------------

#----------------------------------------------------------------------------------

#----------------------------Installing packages with pip--------------------------

#----------------------------------------------------------------------------------

#--------------------------------List Compression----------------------------------

#----------------------------------------------------------------------------------

#----------------------------------Polymorphism------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Operator Overloading------------------------------

#----------------------------------------------------------------------------------