config = {}

print("===== APP CONFIG STORE =====")

app_name = input("Enter App Name : ")
version = float(input("Enter Version : "))
debug = input("Debug Mode(True/False) : ").lower()
max_user = int(input("Enter Max User : "))



# Validation

if isinstance(app_name,str) :
    config['app_name'] = app_name

elif isinstance(version,float) :
    config['version'] = version

if debug in ["true",'false'] :
    config['debug'] = (debug=="true")

if isinstance(max_user, int) and max_user > 0 :
    config['max_user'] = max_user

print("\n===== STORED CONFIG =====\n")

for key, value in config.items() :
    print(f"{key:<12}: {value}")




