w = int(input ())
l = float(input())
k = int (float (w) // l ** 2)
if k < 18.5:
	print ('Underweight')
elif k >= 18.5 and k < 25.0:
	print ('Normal')
elif k >= 25.0 and k < 30.0:
	print ('Overweight')
elif k > 30.0:
	print ('Obesity')