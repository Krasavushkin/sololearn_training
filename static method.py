class Shape:
	def __init__(self, w, h):
		self.w = w
		self.h = h
	def area (self):
		return self.w * self.h


w = int(input())
h = int(input())

r = Shape(w,h)

print(r.area())