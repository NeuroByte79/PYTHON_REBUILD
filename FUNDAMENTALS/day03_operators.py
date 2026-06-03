# ++++++-------> OPERATORS
#@@@@@---------> An operators in python is special symbol or keywords used to perform operation on variables and values.


# @@@@@@++++ python categorized operators into several groups 
# 1. ARITHMETICS OPERATORS
""" (i). Addition (+)  ---> A + B
    (ii). Subtraction (-) ---> A - B
    (iii). Multiplication (*) ----> A * B
    (iv). Division (/) -----> A / B
    (v). Floor Division (//) ----> A // B
    (vi). Modulus (%) ------> A % B
    (Vii). Exponential (**) -----> A ** B
"""
print("Addition : ", 23 + 45,"\n")
print("Subtraction : ", 45 - 15,"\n")
print("Multiplication : ", 12 * 4,"\n")
print("Division : ", 124 / 9,'\n')
print("Modulus : ", 15 % 2)
print("Floor Division : ", 125//7,'\n')
print("Exponential : ", 12 ** 2,'\n')

# Floating point numbers
print("Floating Number PI : ", 3.14,'\n')
print("Floating Number Gravity : ",9.81,'\n')

# Complex numbers 

print("Complex Number : ", 3 - 9j,'\n')
print("Multiplication of Complex NUmbers : ", (3 - 4j) * (7 - 8j),'\n')

# Declaring variables at the top first 
a  = 19 
b = 7
Total = a + b 
Diff = a - b 
Product = a * b
Division = a / b
Reminder = a % b
Floor_division = a // b
Exponential = a ** b

print("a + b : ",Total,"\n")
print("a - b : ",Diff,'\n')
print("a * b : ",Product,'\n')
print("a / b : ", Division,'\n')
print("a % b : ",Reminder,'\n')
print("a // b : ", Floor_division,'\n')
print("a ** b : ", Exponential,'\n')


# .................... 
# @@@@+++++------>>>>>>>>> You can use 'PEDMAS' in python for more than one arithmetics operations are involve use this.

# calculating perimeter of circle

radius = 21
PI = 3.14
perimeter_of_circle = 2 * PI * radius
print("The perimeter of circle is : ", perimeter_of_circle,'\n')




#+++++------->>>>>>>>> ASSIGNMENTS OPERATORS ++++++------->>>>>>>>>>>>
# Used to assign values to variables

# 1. Basic Assignment operator(=) ---->>> Assign a value to a variable
x = 10
name = "Shyam"

print(x)
print(name)
print("\n")
# 2. Add and Assign (+=) ---->>>> Adds the value and store the result back

# syntax
# x += y #  = x + y

x = 10
x += 5
print(x)
print("\n")
# 3. Subtract and Assign(-=) ---->>>> Subtract and store the result

x = 30
x -= 20
print(x)
print("\n")

# 4. Multiply and Assign (*=) ---->>>>> Multiply and store the value

x = 10
x *= 4
print(x)
print("\n")

# 5. Divide and Assign(/=) ---->>>> Divide and store the value

x = 20
x /= 4
print(x)
print("\n")

# 6. Floor Division and Assign (//=) ------->>>>> Remove decimal part and store

x = 27
x //= 5
print(x)
print("\n")

# 7. Modulus and Assign (%=) ----->>>>>> Store reminder

x = 29
x %= 3
print(x)
print("\n")

# 8. Exponent and Assign (**=) --->>>> Power operator

x  = 2
x **= 5
print(x)
print("\n")

# 9. Bitwise AND Assign (&=)

x = 10
x &= 7
print(x)
print("\n")

# 10. Bitwise OR Assign (|=)

x = 10
x |= 7

print(x)
print("\n")

# 11. Bitwise XOR Assign (^=)

x = 10
x ^= 7 
print(x)
print("\n")

# 12. Left Shift Assign (<<=)

x = 5 
x <<= 2
print(x)
print("\n")

# 13. Right Shift Assign (>>=)

x = 20
x >>= 2
print(x)
print("\n")



# ++++++------->>>>>>  COMPARISON OPERATORS   +++++++++---------<<<<<<<<<<<

# 1 . Equal(==)
print(10==10)

# 2. Not Equal (!=)

print(10 != 5)

# 3. Greater Than (>) or Grater Than Equal (>=)
print(10 > 5)
print(10 >= 5)

# 4. Less Than (<) or Less Than Equal (<=)
print(10<5)
print(10<=15)
print("\n")



# +++++++----->>>>> Logical Operator ++++++---------<<<<<<<<

# 1.  AND 
print(True and True)

# 2. OR
print(True or False)

# 3.  Not
print(not True)
print("\n")


# +++++------->>>>>>>  Membership Operator ++++++---------<<<<<<<<<<<<<<

# 1. in ------>>> Present
name = "Python"
print("P" in name)

# 2. not in ------->>>> Not Present

print("z" not in name)
print("\n")


# ++++++++------>>>>>> Identity Operator +++++++++------<<<<<<<<<<<<

# 1. is ----->>>>> Same object

a = [2,3]
b = a

print(a is b)

# 2. is not ------>>>>> Different object

a = [1,2]
b = [1,2]

print(a is not b)
print("\n")

