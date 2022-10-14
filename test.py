from ctypes import LittleEndianStructure


# variables

name="Kiki"
age=33
name1="Lilia"
HEIGHT=153
my_name="Riri"
_name="Ryan"

# for, if, while, import have specific meaning, therefore cant be used as variables names


#----------------------------------------------------------------------------------

#expressions and statements



#expression is any sortf of code that return a value

1+1  #this gonna return 2
"Kiki" #this gonna return string Kiki



#statement is operation on a value

name2="Rose"
print(name2)

#above can be written like this too :  name2="Rose" ; print(name2)  2 statements in one single line separated by semicolon

#----------------------------------------------------------------------------------

#comment

#using hash mark (#) to comment a code. everything after the hash mark is ignored.

#indentation 

#indentation in python matters, has a meaning. everything indented belongs to a block like a control statement or conditional block or function or a class body


#----------------------------------------------------------------------------------

#Data Types

#string
name3="Beau"

#checking data types method 1
print(type(name3)) #will return <class 'str'> at the console

#checking data types method 2 (by comparing it)
print(type(name3)== str) #will return True at the console

#or
print(isinstance(name,str)) #will return True at the console



#number
amount1=2
print(isinstance(amount1,int)) #will return True at the console
print(isinstance(amount1,float)) #will return False
print(isinstance(amount1,str)) #will return False

amount2=2.9
print(isinstance(amount2,float)) #will return True

