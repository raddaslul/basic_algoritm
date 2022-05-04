shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "사이다"]


def is_available_to_order(menus, orders):
    menus.sort()
    for order in orders:
        if not binary_search(menus, order):
            return False
    return True


def binary_search(menus, order):
    min_index = 0
    max_index = len(menus) - 1
    mid_index = (min_index + max_index) // 2
    while min_index <= max_index:
        if menus[mid_index] == order:
            return True
        elif menus[mid_index] > order:
            max_index = mid_index - 1
        else:
            min_index = mid_index + 1
        mid_index = (min_index + max_index) // 2
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
