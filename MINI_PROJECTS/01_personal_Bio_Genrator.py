# Basic version

name = input("Enter full name : ")
age = input("Enter Age : ")
City = input("Enter City : ")
Role = input("Enter Job/Role : ")
College = input("Enter College name : ")
Skills = input("Enter top three skills(comma-sep) : ").strip(",")

print("\n" + "=" * 40)
print("            PERSONAL BIO ")
print("=" * 40)
print(f"Name          : {name}")
print(f"Age           : {age}")
print(f"City          : {City}")
print(f"Role          : {Role}")
print(f"College       : {College}")
print(f"Skills        : {Skills}")
print("=" * 40)
