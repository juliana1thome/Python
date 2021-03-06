# List
x = [4, True, 'hi']
y = 'hi'
print(len(x), len(y))
print("*********************************************************")

print(x.pop())# This will print hi and remove from the list, since it is the last element
print(x)
print("*********************************************************")

x.append('hello')
print(len(x), len(y))
print("*********************************************************")

x.extend([4, 5, 5, 5])
print(len(x), len(y))
print("*********************************************************")

print(x[4])
x[4] = 'hello'
print(x[4])
print("*********************************************************")

# Copy
g = x[:] # You can change this copy and it will not change the real thing
print(g)
print("*********************************************************")

# Tubules --> it is a list that we cannot change, it is immutable
x = (0, 0, 2, 2)

# Also we can do this x =[(),[],[1, 2, 3]]
