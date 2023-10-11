def solution(array1, array2):
    array2.sort()
    array1.sort()

    for item1, item2 in zip(array1, array2):
        if item1 != item2:
            return print(item1)


print("test 1: ")
print("[1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]")
solution([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
print("*********************************************************" + '\n')