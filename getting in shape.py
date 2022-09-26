file = open("/usercode/files/pull_ups.txt")
n = int(input())

lines = file.readlines()[n]
print (lines)

file.close()