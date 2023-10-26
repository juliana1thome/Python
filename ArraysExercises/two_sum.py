def two_sun(num_array, target):
    num_map = {}
    n = len(num_array)

    for i in range(n): # Go through each index (so, it is easy to save it)
        complement = target - num_array[i]
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num_array[i]] = i

    return []  # No solution found

# Test the function
assert (two_sun([1,2,4,8,4,1], 10)) == [1, 3]