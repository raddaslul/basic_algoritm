finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    min_array = 0
    max_array = len(array) - 1
    mid_array = (min_array + max_array) // 2

    while min_array <= max_array:
        if array[mid_array] == target:
            return True
        elif array[mid_array] > target:
            max_array = mid_array - 1
        else:
            min_array = mid_array + 1
        mid_array = (min_array + max_array) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
