# Anagram Check
def anagram(word1, word2):
    # Remove spaces and convert to lowercase
    word1 = word1.replace(' ', '').lower()
    word2 = word2.replace(' ', '').lower()

    # Check for different word lengths
    if len(word1) != len(word2):
        return False

    # Create dictionaries to count letter occurrences
    count1 = {}
    count2 = {}

    # Populate the dictionaries
    for letter in word1:
        count1[letter] = count1.get(letter, 0) + 1

    for letter in word2:
        count2[letter] = count2.get(letter, 0) + 1

    # Compare the dictionaries
    return count1 == count2

# Test the function
assert(anagram("listen", "silent")) == True
assert(anagram("hello", "world")) == False
assert(anagram("doog", "good")) == True
