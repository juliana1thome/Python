for i in range(1, 10, 2):
    print(i)

for i in range(10, 1, -2):  # It is not going to reach 1
    print(i)

for i in [3, 4, 42, 1]: # It will print each of this elements
    print(i)

x = [3, 4, 42, 3, 2, 4]
for i in range (len(x)): # to keep track of i
    print(x[i])

# OR, the combination of everything THE BEST ONE

for i, element in enumerate(x):
    print(i, element)