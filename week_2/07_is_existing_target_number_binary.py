finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, numbers):
    numbers.sort()
    min_arr = 0
    max_arr = len(numbers) - 1
    mid_arr = (min_arr + max_arr) // 2
    while min_arr <= max_arr:
        if numbers[mid_arr] == target:
            return True
        elif numbers[mid_arr] > target:
            max_arr = mid_arr - 1
        else:
            min_arr = mid_arr + 1
        mid_arr = (min_arr + max_arr) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
