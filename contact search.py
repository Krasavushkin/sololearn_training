contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

a, b, c, d, e = contacts
name = input ()
if name in a:
	print (a[0] + ' is '+ str(a[1]))
elif name in b:
	print (b[0] + ' is '+ str(b[1]))
elif name in c:
	print (c[0] + ' is '+ str(c[1]))
elif name in d:
	print (d[0] + ' is '+ str(d[1]))
elif name in e:
	print (e[0] + ' is '+ str(e[1]))
else:
	print ("Not Found")

