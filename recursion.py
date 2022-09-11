def convert(num):
   while num > 0:
      return (num % 2 + 10 * convert(num // 2))
   else:
      return 0
d = int(input())
print (convert(d))