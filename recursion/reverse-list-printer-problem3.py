def reverse_list_printer(some_list, list_length):
    """Takes a list and the length of the list and 
    recursively prints the elements of the list in reverse order"""
    # Base case
    if list_length == 0:
        return
    #Recursive bits
    print(some_list.pop())
    list_length = len(some_list)
    reverse_list_printer(some_list, list_length)

my_list = [1, 2, 3, 4, 5, 6]
the_length = len(my_list)
reverse_list_printer(my_list, the_length)