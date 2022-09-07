price = int(input())
perc = int(input())

res = (lambda x,y: x*y*0.01)(price, perc)

print(res)
