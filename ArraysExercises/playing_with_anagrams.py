# Anagram Check

def anagram(word1, word2):
    # Check if any word has spaces on it, if yes remove it by using replace
    # Make the words by in lowercase
    word1 = word1.replace(' ', '').lower()
    word2 = word2.replace(' ', '').lower()
    word_1_dictionary = {}

    # First check: If the words has different length they can't be an anagram
    if len(word1) != len(word2):
        return False

    else:
        # For each word create a dictionary
        # with the keys being the letters and the value
        # being the amount of times this letter is in the word
        for letter in word1:
            if letter in word_1_dictionary:
                word_1_dictionary[letter] += 1
            else:
                word_1_dictionary[letter] = 1

        for j in word_1_dictionary:
            if word_1_dictionary[j] != 0:
                return False

    return True

print (anagram("doog", "good"))