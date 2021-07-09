# Dictionaries works as the same thing as in c# | You need a key to access a value on it
# Example:
x = {'Key': 4}

print("Dic x values:")
print(x['Key'])
print("*********************************************************")

# Other way to represent it
x['Key2'] = 5
x['Key3'] = [2, 2, 1, 1]

print("Print the values of the key3")
print(x['Key3'])
print("*********************************************************")


print("Dic x value:")
print(x['Key2'])
print("*********************************************************")


# Check if this key is in the dictionary
print('Key' in x)
print("*********************************************************")


# Get all the values of the dictionary
print("Dic x value not in a list:")
print(x.values())
print("*********************************************************")

# But you will want to put this in a list. To look like this:
print("Dic x values in a list:")
print(list(x.values()))
print("*********************************************************")

# Delete an element
del x['Key']
print("Dic List with one key removed:")
print(list(x.values()))
print("*********************************************************")

# ForLoop: This will return all the keys and its values
for key, value in x.items():
    print(str(key) + ", Its value is: " + str(value))
print("*********************************************************")

# Or
for key in x:
    print(str(key) + ", Its value is: " + str(x[key]))