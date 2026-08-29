# Conversion factor
KM_TO_MILES = 0.621371
KG_TO_POUNDS = 2.20462

print("===== UNIT CONVERTER =====")
print("1. KM -> Miles")
print("2. Miles -> KM")
print("3. Celsius -> Fahrenheit")
print("4. Fahrenheit -> Celsius")
print("5. KG -> POUNDS")
print("6. POUNDS -> KG")

choice = input("Enter your choice(1 - 6) : ")

value = float(input("Enter Value : "))

if choice == "1":
    result = value * KM_TO_MILES
    print(f"{value}KM : {result:.2f}MILES")
elif choice == "2":
    result = value / KM_TO_MILES
    print(f"{value}MILES : {result:.2f}KM")
elif choice == "3" :
    result = (value * 9/5) + 32
    print(f"{value}Celsius : {result:.2f}Fahrenheit")
elif choice == "4" :
    result = (value - 32) * 5/9
    print(f"{value}Fahrenheit : {result:.2f}Celsius")
elif choice == "5" :
    result = value * KG_TO_POUNDS
    print(f"{value}KG : {result:.2f}PUNDS")
elif choice == "6" :
    result = value / KG_TO_POUNDS
    print(f"{value}PUNDS : {result:.2f}KG")
else:
    print(f"Invalid Choice !")
