def rev_word(s):
    l = s.split()
    reverse_list = []

    for i in range(len(l) - 1, -1, -1):
        reverse_list.append(l[i])

    print(" ".join(reverse_list))



print("test 1: ")
print('Hi John,    are you   ready to go?')
rev_word('Hi John,    are you   ready to go?')
print("*********************************************************" + '\n')