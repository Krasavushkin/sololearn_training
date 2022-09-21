text = input()
text_split = text.split()
x = len(text_split)

#for w in text:
#	x = text.count(w)
l = 0
for i in text_split:
	l += len(i)
print (l/x)