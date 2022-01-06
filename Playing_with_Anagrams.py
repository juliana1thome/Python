# Anagram Check
from re import split


def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    d1 = {}

    # First check
    if len(s1) != len(s2):
        return False

    else:
        for letter in s1:
            if letter in d1:
                d1[letter] += 1
            else:
                d1[letter] = 1

        for j in d1:
            if d1[j] != 0:
                return False

    return True

anagram("doog", "good")