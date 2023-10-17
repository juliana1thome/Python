def revert_sentence(sentence):
    # Easy solution: it will split the words that have spaces into elements in an array
    # return " ".join(reversed(sentence.split()))

    # Manual Solution
    words = []
    length = len(sentence)
    space = [' ']

    # Tracker of which index we are at
    i = 0

    # While the index is smaller than the length continue
    while i < length:
        # If a space was not found continue
        if sentence[i] not in space:

            # Since this element with index i is not a space it means that it is a word start
            word_start = i

            # Now lets get the end of this word
            # Do this until you find a space and the index did not found the end of the sentence
            while i < length and sentence[i] not in space:
                i += 1

            # On the array of found words make it add the beginning of the word until the end
            # This basically does what the split would do
            words.append(sentence[word_start:i])
        i += 1

    print(' '.join(reversed(words))) # The join here will add spaces to the words and reversed will revert the array
    return " ".join(reversed(words))

# Test the function
assert (revert_sentence("Hi John, are you ready to go?")) == "go? to ready you are John, Hi"