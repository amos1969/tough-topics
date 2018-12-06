def list_printer(some_list):
    """Takes a list and the length of the list and 
    recursively prints the elements of the list"""
    # Base case
    # Empty lists return False as a boolean
    if not some_list:
        return
    # Recursive parts
    # Pop removes the specified item from the list and returns it
    print(some_list.pop(0))
    # We've removed the item so we can just pass the shorter list in to the function call
    list_printer(some_list)

my_list = [1, 2, 3, 4, 5, 6]
list_printer(my_list)