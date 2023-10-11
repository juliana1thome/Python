# Condition
x = 'hello'
y = 'hello'

print(x == y, x != y)

print('a' > 'Z')
print('a=' , ord('a'),'Z=' ,ord('Z'))

# Chained Conditionals
# ***OR*** --> If the result1 is true or result2 is true the entire thingy is true.
# So, if at least one is true the equality will be true too

# ***AND*** --> If there is one false the entire thingy is false. same idea of or but the opposite

# ***NOT*** --> It flips the result, like if it is true it will be false after the not

x = 7
y = 8
z = 0

result1 = x == y
result2 = y > x
result3 = z < x + 2

result4 = result1 or result2 or result3
# The equality must to be true or false

print(result4)

print(not (False and True)) # this is true because it was suppose to be false

