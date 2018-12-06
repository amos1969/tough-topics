def reverse_list_printer(some_list):
    """Takes a list and the length of the list and 
    recursively prints the elements of the list"""
    # Base case
    # Empty lists return False as a boolean
    if not some_list:
        return
    # Recursive parts
    # Pop removes the last item from the list if we don't pass in a index and returns it
    print(some_list.pop())
    # We've removed the item so we can just pass the shorter list in to the function call
    reverse_list_printer(some_list)

my_list = [1, 2, 3, 4, 5, 6]
reverse_list_printer(my_list)