# Data_type And type_casting
# ---->>>> variable can store different type of data ,and different type of data can do different thing
# In python data-type
"""  @@@@@+++++++++ Built-in Data-Type

   Text_type = str(string use to store text)
   
   Numeric_Types = int(integers) , float(decimal numbers), complex(numbers with complex and imaginary part) 
   
   Sequence_Type = list(mutable collection of different type of data), tuple(immutable collection of different type of data), range(Sequence of numbers)
   
   Mapping_Types = dict(key-value pairs for efficient lookup)
   
   Set_Type = set(immutable collection of unique element),and frozenset(immutable version of set)
   
   Boolean_Type = bool(represent True or False)
   
   Binary_Type = bytes, bytearray , and memoryview(used for handling row binary data)
   
   None_type = NoneType(Represent the absence of a value of null value)
   
"""
# 1. string type 
name = "shyam"
sentence = "what is your feature plan ? , Explain the plan in front of me."
Doing_what = "Learning python"

print(name,"\n")
print(sentence,"\n")
print(Doing_what,"\n")

# integer type ---->>> Whole number without decimal.
x = 23
y = 66237547821
z = -23353412

print(x,'\n')
print(y,'\n')
print(z,'\n')

# float type ------>>>> Real numbers with a decimal point 

a = 23.9078976967697
b = -45.9089898797896778

print(a,'\n')
print(b,'\n')

# complex type ------->>>>> Numbers with real and imaginary part

z = 2 + 3j
c = 7 -9j

print(z,'\n')
print(c,'\n')

# list type ------>>>> Mutable(changeable) ordered collection of different data type

lst = [12,23,"Shyam",35]

print(lst,'\n')

# @@@--->> you can also print length of list,tuple,dictionary,string using len() function
# @@@--->> you can check type using type() function of any data type

print(len(lst),'\n')

# tuple type ---->>>>>  Immutable(unchangeable) ordered collection of different data type
tpl = ("shyam","baghel",678,"mango")
print(tpl,'\n')

# dictionary type ------>>>> Dictionary for efficient data retrieval via unique keys

dct = {"name" : "Baghel","age" : 19,"is_student" : True}
print(dct,'\n')
print(len(dct),'\n')

# set type ----->>>>>> Mutable collection with no duplicate items 

sts = {12,14,"shyam"}
print(sts,'\n')
print(len(sts),'\n')






#           @@@@@@@@@@@++++++++ Type Casting ++++++++++@@@@@@@@@@@@@

# you can not convert string into any other like int ,float,complex but int ,float , convert str


# 1. int to str

a = 24 
print(type(a),'\n')    # you can print type of data type using type() function
b = str(a)
print(type(b),'\n')


# 2. int to float

x = 34
print(type(x),'\n')
y = float(x)
print(type(y),'\n')

# float to str

z = 67.898979
print(type(z),'\n')
print(type(str(z)),'\n')

# float to int

i = 45
print(type(i),'\n')
print(type(float(i)),'\n')

