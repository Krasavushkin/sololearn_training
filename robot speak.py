n= int(input())
if n>=11 and n<=19 or n%100>=11 and n%100<=19:
    print('В комнате ' + str(n) + ' программистов')
elif n > 1 and n <= 4 or n%10 > 1 and n%10 <= 4:
    print('В комнате ' + str(n) + ' программиста')
elif n > 4 and n <= 20 or n%10 > 4 and n%10 <= 9 or n == 0 or n %10 == 0:
    print('В комнате ' + str(n) + ' программистов')
elif n == 1 or n%10 == 1:
    print('В комнате ' + str(n) + ' программист')