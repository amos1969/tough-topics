def get_minimum(some_list):
    """Takes a list of integers and recursively finds the minimum value which it returns"""
    # Get the
    current_value = some_list.pop()
    # Base case
    if not some_list:
        return current_value
    # You could actually just get the minimum from a list by doing min
    return min(current_value, get_minimum(some_list))


my_list = [4, 2, 5, 4, 2]
print(get_minimum(my_list))