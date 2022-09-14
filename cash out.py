def withdraw(amount):
    print(str(amount) + " withdrawn!")


x = input()
try:
    int(x)
    withdraw(x)
except (ValueError, TypeError, SyntaxError):
    print("Please enter a number")
