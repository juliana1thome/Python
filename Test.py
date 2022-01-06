def solution(l, t):
    missing_dic = {}

    sum = 0

    # First check: check if the sum of all elements is smaller than t
    for element in l:
        sum += element
    if sum < t:
        return print([-1, -1])

    else:
        for element in l:
            # Save the value that is missing for t
            missing = t - element
            missing_dic = [element] = missing


print("test 1: ")
print("[1, 2, 3, 4] t: 15")
solution([1, 2, 3, 4], 15)
print("*********************************************************" + '\n')

print("test 2: ")
print("[4, 3, 10, 2, 8] t: 12")
solution([4, 3, 10, 2, 8], 12)
print("*********************************************************" + '\n')
