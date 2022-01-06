def solution(s):
    s.lower()
    save = []
    i = 0

    while i < len(s):
        for letter in s:
             if letter not in save:
                save.append(letter)
                i += 1

             else:
                return print(False)
    return print(True)


print("test 1: ")
print('aaabc')
solution('aaabc')
print("*********************************************************" + '\n')

print("test 2: ")
print('abc')
solution('abc')
print("*********************************************************" + '\n')

print("test : ")
print('abcdea')
solution('abcdea')
print("*********************************************************" + '\n')