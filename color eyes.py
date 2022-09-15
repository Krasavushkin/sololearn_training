data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]
color = str(input())
x = 23+11+5+14+8+32+20+5

if color == 'brown':
	print(int((data[0][0] + data[1][0]) *100/x))
elif color == 'blue':
	print(int((data[0][1] + data [1][1]) *100/x))
elif color == 'green':
    print(int((data[0][2] + data [1][2]) *100/x))
else:
	print(int((data[0][3] + data [1][3]) *100/x))