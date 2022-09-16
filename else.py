menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']
x = input()
try:
   str(x)
   print (menu[int(x)])
   print('Thanks for your order')
except:
   print ('Item not found')