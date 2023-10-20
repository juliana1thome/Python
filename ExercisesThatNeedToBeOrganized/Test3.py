from itertools import combinations

def solution(l, t):
    sum_of_elements = sum(l)
    combinations_arr = []
    result_list = []

    # First check: l must contain 1 to 100 elements
    if 1 > len(l) > 100:
        return print("-1, -1")

    # Second check: l elements must be between 1 to 100
    for k in l:
        if 1 > k > 100:
            return print("-1, -1")

    # Third check: t must be smaller or equal to 250
    if 1 > t > 250:
        return print("-1, -1")

    # Forth check: check if the sum of all elements is smaller than t
    if sum_of_elements < t:
        return print("-1, -1")

    # Add all combinations to an array of combinations
    for i in range(len(l)):
        # print(list(combinations(l, i)))
        combinations_arr += list(combinations(l, i)) # I used i to tell how long the combinations should be
        # print(combinations_arr)

    for item in combinations_arr:
        if sum(item) == t: # Sum all elements of each sublist of combinations_arr and check which is = to t
            result_list.append(item)

    for j in result_list:
        k1 = j[0]
        k2 = j[1]
        y1 = l.index(k1)
        y2 = l.index(k2)

    return print(str(y1) + ", " + str(y2))

print("test 1: ")
print("[1, 2, 3, 4] t: 15")
solution([1, 2, 3, 4], 15)
print("*********************************************************" + '\n')

print("test 2: ")
print("[4, 3, 10, 2, 8] t: 12")
solution(range(1, 10000), 12)
print("*********************************************************" + '\n')