"""
Repl Tutorial 130. Exercise: Pets Everywhere
Lukas Maynard
SDEV - 220
Practiced: map(), lambda functions, and sort()
"""
# One line lambda expression that prints a squares list
mylist = [5,4,3]
print(list(map(lambda i:i**2, mylist)))

# Sort a list of tuples by the second value by declaring the key with a lambda function
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda i:i[1])
print(a)
