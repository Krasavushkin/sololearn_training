def better_than_average(class_points, your_points):
    if your_points > class_points:
        print (True)
    else:
        print (False)

class_points = list(input())
your_points = list(input())

better_than_average(class_points, your_points)