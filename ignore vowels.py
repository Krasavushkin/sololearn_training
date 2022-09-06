word = input ()

letters = ['b', 'c', 'd', 'f', 'h', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'w', 'x', 'z']

check = [ i for i in word if i in letters]

print (check)