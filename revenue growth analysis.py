data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
age = int(input())
values = data.values()
old_age = 18
new_adult = 0
new_child = 0
old_adult = 0
old_child = 0
for value in values:
	if value >= age:
		new_adult += 1
	elif value < age:
		new_child += 1
	if value >= old_age:
		old_adult += 1
	elif value < old_age:
		old_child += 1
old_price = old_adult * 20 + old_child * 5
new_price = new_adult * 20 + new_child * 5

#print (old_adult)
print (int(((new_price - old_price)/old_price)*100))
