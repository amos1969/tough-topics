def zero_counter(some_list):
    """Takes a list of integers and returns the number of zeroes found
    inside the list"""
    # Base Case
    if not some_list:
        return 0
    # Remove the last value from the list
    current_value = some_list.pop()
    if current_value == 0:
        # Return 1 and the sum of the other zeroes
        return 1 + zero_counter(some_list)
    else:
        # Return 0 and the sum of the other zeroes
        return 0 + zero_counter(some_list)

my_list = [1, 2, 5, 0, 0, 8, 0, 5, 1]
# Should output 3
print(zero_counter(my_list))
