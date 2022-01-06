def solution(l, t):
    sum_of_elements = sum(l)
    we_have_a_problem_result = [-1, -1]

    # First check: l must contain 1 to 100 elements --> OK
    if not 1 <= len(l) <= 100:
        return we_have_a_problem_result

    # Second check: l elements must be between 1 to 100 --> OK
    if max(l) > 100 or min(l) < 1:
        return we_have_a_problem_result

    # Third check: t must be smaller or equal to 250 --> OK
    if not 1 <= t <= 250:
        return we_have_a_problem_result

    # Forth check: check if the sum of all elements is smaller than t --> OK
    if sum_of_elements < t:
        return we_have_a_problem_result

    # Obvious check: if the the sum of all elements is equal than t, it should return the entire array --> OK
    if sum_of_elements == t:
        return [0, (len(l) - 1)]

    # This for will fixate the start index
    for start_index, element in enumerate(l):

        # The current sum will start as the first element, and now the end index is the start one
        current_sum = element
        end_index = start_index

        # This for will continue the continuous sum, until some condition interrupt it
        for el in l[start_index + 1:]:

            # Is the current sum equal to t, if yes return the start index, and the end index
            if current_sum == t:
                return [start_index, end_index]

            # Is the current sum + element equal to t, if yes
            elif current_sum + el == t:
                end_index += 1
                return [start_index, end_index]

            # Is current sum smaller than t, if yes continue
            elif current_sum < t:
                end_index += 1
                current_sum += el
                continue

            # Is current sum bigger than t, if yes break it
            elif current_sum > t:
                break

            # It should never get here
            else:
                raise ValueError

    return [-1, -1]


"""Tests"""

assert solution([1, 5, 1, 3], 8) == [-1, -1]

assert solution([1, 2, 3, 4], 15) == [-1, -1]

assert solution([4, 3, 10, 2, 8], 12) == [2, 3]

assert solution([3, 3, 3, 3], 12) == [0, 3]

assert solution([4, 3, 5, 7, 8], 12) == [0, 2]

assert solution([4, 3, 10, 2, 8], 50) == [-1, -1]

assert solution([4, 6, 16, 10, 5, 10], 15) == [3, 4]

assert solution(range(1, 1000), 12) == [-1, -1]

assert solution(range(1, 100), 12) == [2, 4]

assert solution([], 12) == [-1, -1]

assert solution([4, 300, 10, 2, 8], 12) == [-1, -1]

assert solution([12], 12) == [0, 0]
