x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = ['hi', 'hello', 'goodbye', 'tchau', 'cya']
s = 'hello'

# It works with a start : stop : step
sliced = x[0:3:2]
print(sliced)

sliced = x[0:4:2]
print(sliced)

# Reverse a list
sliced = x[::-1]
print(sliced)

# Remove just one letter
sliced = s[::2]
print(sliced)

# Just one : Says stop in the ... position
sliced = s[:2]
print(sliced)

# After the number just one : says start from this position, same as ::
sliced = s[2:]
print(sliced)