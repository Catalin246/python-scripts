try:
    age = int(input("Please enter your age: "))
except:
    print("An exception occured")

if age < 18:
    print("You are an minor.")
elif age < 64:
    print("You are an adult")
else:
    print("You are a senior")