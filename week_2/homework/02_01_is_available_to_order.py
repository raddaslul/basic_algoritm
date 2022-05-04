shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "사이다"]


# def is_available_to_order(menus, orders):
#     menus.sort()
#     for order in orders:
#         if not is_exist_target_number_binary(order, menus):
#             return False
#     return True
#
#
# def is_exist_target_number_binary(target, numbers):
#     numbers.sort()
#     min_arr = 0
#     max_arr = len(numbers) - 1
#     mid_arr = (min_arr + max_arr) // 2
#     while min_arr <= max_arr:
#         if numbers[mid_arr] == target:
#             return True
#         elif numbers[mid_arr] > target:
#             max_arr = mid_arr - 1
#         else:
#             min_arr = mid_arr + 1
#         mid_arr = (min_arr + max_arr) // 2
#     return False

def is_available_to_order(menus, orders):
    # menus_set = list(menus)
    # print(menus_set)
    for order in orders:
        if order not in menus:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
