from collections import OrderedDict

def string_compression(string):
    # This function has the intent to get a string and create
    # another one that will have the letter and the amount of times it appeared on the string
    # A and a are different this pattern will be followed by the other letters and characters

    # Because I'm lazy I will use dictionary
    dict = {}

    # Lets consider that the final string is nothing
    final_string = ""

    # First check if array is of length = 0
    if len(string) == 0:
        return 0

    # For each element on the string if the element is on the dictionary already make the value be += 1
    # Otherwise make it be the first one and make the value be = 1
    for element in string:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1

    # After that just transform the dict into a string again
    for key, value in dict.items():
        final_string += str(key) + str(value)

    print(final_string)
    return final_string

# Test the function
# Python 3.6 the standard dict type maintains insertion order by default
# However since I'm currently using 2.7 this is not the case
assert (string_compression("AAAAABBBBCCCC")) == 'A5C4B4'
assert (string_compression("AAaaaBBBBCCCC")) == "A2a3C4B4"
