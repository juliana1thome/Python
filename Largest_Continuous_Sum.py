def solution(array):
    current_sum = 0
    max_sum = 0

    if len(array) == 0:
        return 0

    for item in array:
        # The current sum will be the current sum + item or the item if it is bigger
        current_sum = max(current_sum + item, item)
        # print(current_sum)
        max_sum = max(current_sum, max_sum)
    return print(max_sum)


print("test 1: ")
print("[1, 2, -1, 3, 4, 10, 10, -10, -1]")
solution([1, 2, -1, 3, 4, 10, 10, -10, -1])
print("*********************************************************" + '\n')