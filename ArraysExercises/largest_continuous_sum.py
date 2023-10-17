def large_continuous_sum(array):

    # First check if array is of length = 0
    if len(array) == 0:
        return 0

    # Start the max and current sum at the first element
    max_sum = current_sum = array[0]

    # For every element in array
    # Note: [1:] makes me skip the first element
    # I'm skipping the first element since I considered it to be the current sum which is the max sum
    for element in array[1:]:
        # Set current sum as the higher of the two
        # Basically define the current sum, by checking if the current sum + the element is bigger than the element itself
        current_sum = max(current_sum+element, element)

        # Set max as the higher between the current_sum and the current_max
        max_sum = max(current_sum, max_sum)

    return max_sum

# Test the function
assert (large_continuous_sum([1,2,-1,3,4,10,10,-10,-1])) == 29