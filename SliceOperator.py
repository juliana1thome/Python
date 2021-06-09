x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = ['hi', 'hello', 'goodbye', 'tchau', 'cya']
s = 'hello'

# It works with a start : stop : step
sliced = x[0:3:2]
print(sliced)

sliced = x[0:4:2]
print(sliced)

# reverse a list
sliced = x[::-1]
print(sliced)

# Remove just one letter
sliced = s[::2]
print(sliced)
