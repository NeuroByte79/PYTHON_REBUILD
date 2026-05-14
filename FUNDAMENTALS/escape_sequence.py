# Escape Sequence in Python 

# ----->>>>> Escape sequence e special character combination used inside string.
"""They start with a Backslash '\' and tell python to perform a special action instead of 
   treating characters normally
"""

# Basic syntax
"Hello\nWorld"

"""\n in escape sequence 
   @ it means "new line"
"""

# +++++++++++++ Most important Escape Sequence ++++++++++++++++#

# 1. New line - \n (move text to next line)

print("python\njava")

# 2. Tab space - \t (Add tab spacing)

print("Shyam\tBaghel")

# 3. Backslash - \\ (Used to print actual backslash)

print("C:\\Users\\Shyam")

# 4. Single Quotes - \' (used to insert single quotes inside single-quoted string)

print("It\'s Python")

# 5. Double Quotes - \" (Used to insert double quotes inside double-quoted strings)

print("He said \"Hello\"")

# 6. Backspace - \b (Removes one character before it)

print("Hell\bo")

# 7. Carriage Return - \r (Moves Cursor to beginning of line)

print("12345\rABC")

# 8. Unicode Characters — \u (Used for Unicode symbols)

print("\u03A9")

# 9. ASCII / Character Codes — \x (Hexadecimal character representation)

print("\x41")