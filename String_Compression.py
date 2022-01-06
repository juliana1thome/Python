def solution(s):
    d1 = {}
    final_string = ""

    # Step One: check if how many of each letter exist
    for letter in s:
        if letter in d1:
            d1[letter] += 1
        else:
            d1[letter] = 1

    # Step Two: transform dictionary into a string
    for char, count in d1.items():
        final_string += str(char) + str(count)
    print(final_string)


print("test 1: ")
#print('AAAAABBBBCCCC')
solution('AAAAABBBBCCCC')
print("*********************************************************" + '\n')

print("test 2: ")
#print('AAaaaBBBBCCCC')
solution('AAaaaBBBBCCCC')
print("*********************************************************" + '\n')