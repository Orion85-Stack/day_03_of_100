# check if input from user is even / odd

number =int(input("Please input a number\n"))

calc = number % 2

if calc == 0:
    print("The number is even")
else:
    print("The number is odd")