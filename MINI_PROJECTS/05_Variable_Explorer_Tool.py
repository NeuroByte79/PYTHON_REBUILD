import sys

value = eval(input("Enter a value : "))

print("\n" + "="*40)
print(f"{'VARIABLE EXPLORER':^40}")
print("="*40)

print(f"{'value':<15}: {value}")
print(f"{'Type':<15}: {type(value).__name__}")
print(f"{'Memory ID':<15}: {id(value)}")
print(f"{'Size':<15}: {sys.getsizeof(value)} bytes")
print(f"{'Truthiness':<15}: {bool(value)}")

print("="*40)
