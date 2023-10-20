num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# Simple version 1
result = num1 + num2
print(result)
# The problem with this is that by default it will be a string
# So to fix this I need to transform the numbers into numbers

# Simple version 2
result = float(num1) + float(num2)
print("Correct answer: {}".format(result))
