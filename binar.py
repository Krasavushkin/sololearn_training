n=int(input())
m=n
p=1
d1=0
while m>0:
    d1=d1+m%2*p
    p=p*10
    m=m//2
print(d1)