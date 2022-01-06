def solution(l, t):
    sum_of_elements = sum(l)
    current_sum = 0
    current_sum_list = []
    final_list = []
    we_have_a_problem_result = [-1, -1]
    first_time_using_current_index = True
    current_index = 0
    started_index = 0

    # First check: l must contain 1 to 100 elements --> OK
    if not 1 <= len(l) < 100:
        return we_have_a_problem_result

    # Second check: l elements must be between 1 to 100 --> OK
    if max(l) > 100 or min(l) < 1:
        return we_have_a_problem_result

    # Third check: t must be smaller or equal to 250 --> OK
    if not 1 < t < 250:
        return we_have_a_problem_result

    # Forth check: check if the sum of all elements is smaller than t --> OK
    if sum_of_elements < t:
        return we_have_a_problem_result

    if sum_of_elements == t:
        return [0, (len(l) - 1)]

    while current_index in range(current_index, len(l)):

        # First time using this current index?, if yes save it as start index
        if first_time_using_current_index is True:
            started_index = current_index

        # Is current sum smaller than t, if yes continue summing
        if current_sum < t:
            current_sum += l[current_index]
            current_sum_list.append(l[current_index])
            current_index += 1
            first_time_using_current_index = False

        # Is current sum bigger than t, if yes start all over again
        elif current_sum > t:
            current_sum_list = []
            current_sum = 0
            current_index = started_index + 1
            first_time_using_current_index = True

        # Is current sum equal to t, if yes break loop
        elif current_sum == t:
            break

    for i in range(len(current_sum_list)):
        x = current_sum_list[i]
        final_list.append(l.index(x))

    print(current_sum_list)
    print(final_list)
    return [final_list[0], final_list[-1]]


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
