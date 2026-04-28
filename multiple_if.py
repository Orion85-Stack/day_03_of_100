# Multiple if statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
photo = input("Would you like a photo? Y/N ")

bill = 0

if height >= 120:
    print("You can ride")
    if age <= 12:
        bill = 5
        print("Child ticket is $ 5.")
    elif 12 < age <18:
        bill = 7
        print("Youth ticket is $ 7.")
    else:
        bill = 12
        print("Adult ticket is $ 12.")
    if photo == "Y":
        bill += 3
        print("$ 3 added for photo")
    print(f"Your bill is: $ {bill}")
else:
    print("You can't ride the rollercoaster!")