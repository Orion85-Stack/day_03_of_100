# Logical operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    if age <= 12:
        print("Please pay $ 5.")
    elif 12 < age <18:
        print("Please pay $ 7.")
    elif age >=45 and age <=55 :
        print("Ticket is free.")
    else:
        print("Please pay $ 12.")
else:
    print("You can't ride the rollercoaster!")