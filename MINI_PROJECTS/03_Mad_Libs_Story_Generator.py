print("=== Mad Libs Story Generator ===")

name = input("Enter a name : ")
place = input("Enter a place : ")
animal = input("Enter an animal : ")
Adjective = input("Enter an adjective :  ")
verb = input("Enter a verb : ")

print("\n----- Your Story -----\n")

print(
    f"One day, {name} went to {place}.\n"
    f"While walking around, they show a {Adjective} {animal}. \n"
    f"The {animal} suddenly started to {verb}.\n"
    f"Everyone in {place} was surprised! \n"
    f"In the end, {name} and the {animal} become best friends."
)
