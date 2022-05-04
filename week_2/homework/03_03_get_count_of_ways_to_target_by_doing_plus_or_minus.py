numbers = [2, 3, 1]
target_number = 0
result_count = 0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, cur_index, cur_sum):
    if cur_index == len(array):
        if cur_sum == target:
            global result_count
            result_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, cur_index + 1, cur_sum + array[cur_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, cur_index + 1, cur_sum - array[cur_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(result_count)
