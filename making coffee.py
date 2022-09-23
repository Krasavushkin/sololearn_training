coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input())

try:
    choice == range(5)
    print(coffee[choice])

except:
    print('Invalid number')

finally:
    print('Have a good day')