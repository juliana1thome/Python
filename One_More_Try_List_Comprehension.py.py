def solution(l, t):
    sum_of_elements = sum(l)
    current_sum = 0
    current_sum_list = []
    final_list = []
    we_have_a_problem_result = [-1, -1]
    found = False
    element = 0
    note = 0

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

    while element in range(element, len(l)):
        if found is False:
            note = element
        if current_sum < t:
            current_sum += l[element]
            current_sum_list.append(l[element])
            element += 1
            found = True
        elif current_sum > t:
            current_sum_list = []
            current_sum = 0
            element = note + 1
            found = False
        elif current_sum == t:
            element = 0
            break

    for i in range(len(current_sum_list)):
        x = current_sum_list[i]
        final_list.append(l.index(x))

    return [final_list[0], final_list[-1]]