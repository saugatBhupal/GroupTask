name= input("What is your name? ")
age= int(input("What is your age? "))

if age < 0 :
    print(f"Invalid age")
if age==18 :
    print(f"Dear {name}, you are eligible for voting.")
elif age>18 :
    print(f"Dear {name}, you are eligible for voting. ")
else:
    print(f"Dear {name}, you are not eligible for voting. ")
