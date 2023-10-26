def isPalindrome(int):
    characters = []

    for char in str(int):
        characters.append(char)

    if characters == characters[::-1]:
        return True

    return False

    # # Convert the integer to a string
    # num_str = str(num)
    #
    # # Compare the string with its reverse
    # if num_str == num_str[::-1]:
    #     return True
    #
    # return False


# Test the function
assert (isPalindrome(121)) == True
assert (isPalindrome(-121)) == False
assert (isPalindrome(10)) == False