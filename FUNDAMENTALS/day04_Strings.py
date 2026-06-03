# String ----->>>> String is a sequence of character enclosed in quotes.

name = 'Shyam'

# 1. Creating String ---->>>>>>

# Single Quotes
name = 'Shyam'

# Double Quotes 
name = "Shyam"

# Triple Quotes 

s = """Hello           
world""" # used for multiline string


# String Characteristics 
"""1. Ordered
2. Immutable(can't be changed directly)
3. Iterable 
4. Supports indexing and slicing
5. Can contain latter, numbers, symbols, emojis 
"""

#   String indexing 
s = "Python"
#    012345    ----> positive indexing
#   -6-5-4-3-2-1 ----->> Negative indexing


# Positive indexing 
print(s[0]) # P

# Negative indexing 
print(s[-1])



# String Slicing ------------>>>>>>>>>> Syntax: (string[start:end:step])

s = "Python"
print(s[0:4])    # Pyth
print(s[2:])  # thon
print(s[:4]) # Pyth
print(s[::-1]) # nohtyP   (Reverse the string)

# 1. String Length ----- len(string name)

s = "Python"
print(len(s))


# 2. String Concatenation --------->>>>>>     

a = "Hello"
b = "World"

print(a + b)

# 3. String Repetition ----->>

print("Hii"*3)


# 4.  Membership Operator (in ,not in) ----->>>>>

s = "Python"
print("P" in s)
print("Java" not in s)


#5.  .upper() ---> Convert to uppercase
s = "python"
print(s.upper())

# 6.  .lower() --->>> Convert all lowercase

s = "PYTHON"
print(s.lower())

# 7. .capitalize() --->>>> Convert first latter to capital

s = "python"
print(s.capitalize())

# 8.  .title()  ----->>>> Convert first latter of each word of sentence in capital latter

s = "hello world"
print(s.title())


# 9.  .swapcase()  ----->>>> convert lowercase latter to uppercase or uppercase to lowercase

s = "PyTHon"
print(s.swapcase())   # pYthON

# 10. .casefold()  ---->>> Used for advanced lowercase comparison 
print("HELLO".casefold()) # hello

# 11.  .strip() ---->>>. Removes spaces

s = "   python   "
print(s.strip())

# 12.   .lstrip()  ---->>>>  Removes left spaces
s = "      python"
print(s.lstrip()) 

# 13.    .rstrip() ----->>> Removes right spaces
s = "python      "
print(s.rstrip())


# 14.    .replace(old,new)  ----->>> replace strings
s = "I like java"
print(s.replace("java","Python"))

# 15.  .split() --->>>>> Convert string into list

s = "Python java C++"
print(s.split())


# 16.    .join()   ----->>>> list to string

words = ["I","Love","Python"]
print(" ".join(words))

# 17.  .find()   ----->> Return index 

s = "Python"
print(s.find("t"))
print(s.find("x"))   # -1 if not founded


# 18.  .index()  ------->>>>> give index of latter

print("Python".index("t"))

# if ot found: give ValueError


# 19.    .count() ---->>>> Count the latter apreance in word
print("banana".count("a"))

# 20.   .startswith()  ---->>>>> check Perfix
print("Python".startswith("Py"))

# 21.   .endswith()   ---->>>>>  check sufix
print("Python".endswith("on"))

# 22.   .center()  --->>>centre with padding
print("python".center(20))

# 23.   .ljust()   --->>> left-align a string within a specified total width by adding padding characters to its right side
print("Python".ljust(30))

# 24.   .rjust()  -->>>> used to right-align a string within a specified total width by padding its left side with a chosen
print("Python".rjust(48))


# 25.   .zfill()  --->>>>   method pads a string with leading zeros (0) until it reaches a specified width.

print("45".zfill(7))

# 26.   .isalpha() ----->>> check letter only
print("Python".isalpha())

# 27.  .isdigit()   --->>> check digit only
print("1234".isdigit())