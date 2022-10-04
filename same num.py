a = int(input())
b = int(input())
d = 0
while a>0:
    d += a
    if d%b == 0 and d%a ==0:
        print (d)
        break
