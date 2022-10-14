


#-----------------------------------variables--------------------------------------

name="Kiki"
age=33
name1="Lilia"
HEIGHT=153
my_name="Riri"
_name="Ryan"

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
print("Scamp " + "is a good dog")

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

# print(0 and 1) ## 0
# print(1 and 0) ## 0
# print(False and 'hey') ## False
# print('hi' and 'hey') ## hey
# print([] and False) ## []
# print(False and []) ## False




#--------------Bitwise Operators--------------------
#very rarely uses, only specific situation

#--------------is & in Operators--------------------

#--------------Ternary Operator---------------------


#----------------------------------------------------------------------------------

#--------------------------------Strings-------------------------------------------

#--------------String Methods---------------------

#--------------Escaping Characters----------------

#--------------String Characters & Slicing--------


#----------------------------------------------------------------------------------

#--------------------------------Booleans------------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Number Data Types---------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Built-in Functions--------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Enums---------------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------User Input----------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Lists--------------------------------


#----------Sorting Lists-------

#----------------------------------------------------------------------------------

#--------------------------------Tuples--------------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Dictionaries--------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Sets----------------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Functions-----------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Variable Scope------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Nested Functions----------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Closures------------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Objects-------------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Loops---------------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Break and Continue--------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Classes-------------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Modules-------------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Arguments from Command Line-----------------------

#----------------------------------------------------------------------------------

#--------------------------------Lambda Functions----------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Map, Filter, Reduce-------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Recursion-----------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Decorators----------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Docstrings----------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Annotations---------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------Exceptions----------------------------------------

#----------------------------------------------------------------------------------

#--------------------------------With----------------------------------------------

#----------------------------------------------------------------------------------