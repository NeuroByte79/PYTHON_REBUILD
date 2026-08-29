print("===== STUDENT REPORT CARD =====")

name = input("Enter Student Name : ")

sub1 = float(input("Enter Subject 1 Marks : "))
sub2 = float(input("Enter Subject 2 Marks : "))
sub3 = float(input("Enter Subject 3 Marks : "))
sub4 = float(input("Enter Subject 4 Marks : "))
sub5 = float(input("Enter Subject 5 Marks : "))

total = sub1  + sub2 + sub3 + sub4 + sub5

average = total / 5

percentage = (total/500) * 100

# Garde Calculation

if percentage >= 90 :
    grade = "A+"
elif percentage >= 80 :
    grade = "A"
elif percentage >= 70 :
    grade = "B"
elif percentage >= 60 :
    grade = "C"
elif percentage >= 50 :
    grade = "D"
else :
    grade = "F"

# Pass / Fail

if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and sub4 >= 33 and sub5 >= 33 :
    Status = "PASS"
else :
    Status = "FAIL"

print("\n" + "=" * 40)
print(f"{'STUDENT REPORT CARD':^40}")
print("="*40)

print(f"{'Name':<15}: {name}")
print(f"{'Total':<15}: {total:.2f}")
print(f"{'Average':<15}: {average:.2f}")
print(f"{'Percentage':<15}: {percentage:.2f}")
print(f"{'Grade':<15}: {grade}")
print(f"{'Status':<15}: {Status}")

print("="*40)






