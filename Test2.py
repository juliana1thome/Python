from itertools import combinations

def solution(l, t):

    # Variables
    comb = list(combinations(l, 2))
    comb_sum = list(sum(comb))
    elements_sum = 0

    # First check: checking if the sum of all elements is smaller than t
    for element in l:
        elements_sum += element

    if elements_sum < t:
        return print("[-1, -1]")

    for i in range(comb_sum):
        if comb_sum[i] == t:
            print(comb_sum[i])


print("test 1: ")
print("[1, 2, 3, 4] t: 15")
solution([1, 2, 3, 4], 15)
print("*********************************************************" + '\n')

print("test 2: ")
print("[4, 3, 10, 2, 8] t: 12")
solution([4, 3, 10, 2, 8], 12)
print("*********************************************************" + '\n')
