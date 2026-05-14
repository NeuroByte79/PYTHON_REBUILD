# variables => variable are container that store data in the program
# $$$ python has no command for declaring variables $$$ , variable create at the moment


name = "shyam"
age = 19
city = "gorakhpur"
print(name)
print(age)
print(city)

# *****---> In python do not need to declared type of variables 

# variable names
# ✍️✍️✍️✍️ name of variables are short and meaningful and more descriprive name
"""⧴ Rules for python variables
  1.  variables name must start with latter or the underscore character
  2.  A variables name con't start with a number
  3.  A variable name can only contain alpha-numeric character and underscores(A-z,0-9,_)
  4.  variable name are case-sensitive(age,Age,AGE are three different variable)
  5.  A variable name can't be any python keywords
"""
myvar = "shyam"
myVar = "shyam"
my_var = "shyam"
_myvar = "shyam"
_my_var = "shyam"
MYVAR = "shyam"
myvar2 = "shyam"


# Python variables - Assign multiple value(many value to multiple variables)
# ------> python allows you to assign multiple variable in one line
x ,y, z = "shyam","Ayushi","Harsita"
print(x)
print(y)
print(z)
# --------> Make sure the number of variable matches the number of values ,else you will get an error


# One value to multiple variable 
# ------> you can assign the same value to multiple variable in one line

x = y = z = "Baghel"
print(x)
print(y)
print(z)


# unpack a collection 
# @---->>>>> If you have collection of values in a list or tuple etc. Python allow you to extract the value into variables. This is called unpacking 

names =["Ayushi","Harsita","shyam"]
x , y, z = names
print(x)
print(y)
print(z)


# python Global variable 
# ----->>>>>> Variable that are created outside of a function (all example previously is Global variables)
# $$$$$++++++++    Global variable can be used by everyone , both inside of function or outside +++++++$$$$$


# Create variable outside of function and use inside of function

first_name = "shyam"

def my_name():
    print("My name is",first_name,"\n")

my_name()



# if you create a variable with the same name inside a function  this variable will be local , and can only be used inside the function. The Global variable with same name will remain as it is, global and with the original value.

x = "funy"

def myfun():
    x = "fantastic"
    print("python is",x)
    
myfun()

print("python is",x)


# The Global keyword

# ------>>>>>> Normally, when you create variable inside a function, that variable is local, and can only used inside that function
## To create Global variable inside a function, you can use the 'global' keyword.

name = "shyam"
def my_name():
    global name 
    name = "Baghel"
    print("your name is ",name)
my_name()
print("your name is",name)