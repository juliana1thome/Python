# Note: This actually creates a dictionary
b = {}

# Creating a set
x = set() # Empty set
s = {4, 32, 2, 2, 21, 21}
s2 = {3, 4, 22, 1}
L=[4, 32, 2, 2]

# Sets will be printed in a different order and it will remove repeated numbers
print(s)

# Add element
s.add(5)
print(s)

# Remove element
s.remove(5)
print(s)

# Find element in a set, using false or true
# This operation is much faster in s than L since its in a set
print(4 in L)
print (3 in s)

# Union of sets
print(s.union(s2))

# The difference between sets
print(s.difference(s2))

# S and S2 Intersection
print(s.intersection(s2))