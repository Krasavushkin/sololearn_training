def decor (func):
	def wrap ():
		print ("***")
		func ()
		print ("***")
		print ("END OF PAGE")
	return wrap

g = input()
@decor
def invoice():
    print("INVOICE #" + g)

invoice();