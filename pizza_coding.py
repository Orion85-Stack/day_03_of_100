"""
1. work out how much they need to pay based on their size of choice
2. work out how much to add to their bill based on their pepperoni choice
3. work out their final amount based on whether they want extra cheese
"""
# prices
small_pizza = 15
medium_pizza = 20
large_pizza = 25
xpepperoni = 2
xcheese = 1

greeting = "Welcome to Python Pizza deliveries"
print(greeting)
size = input("What size pizza do you want? S, M, or L ").strip().upper()
pepperoni = input("What pepperoni do you want? Y / N ").strip().upper()
extra_cheese = input("What cheese do you want? Y / N ").strip().upper()

bill = 0

if size == "S":
    bill += small_pizza
elif size == "M":
    bill += medium_pizza
elif size == "L":
    bill += large_pizza
if pepperoni == "Y":
    bill += xpepperoni
if extra_cheese == "Y":
    bill += xcheese
else:
    print("Please enter correct details")

print(f"Your final bill is ${bill}")
