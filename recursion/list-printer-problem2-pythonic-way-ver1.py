def list_printer(some_list):
    """Takes a list and the length of the list and 
    recursively prints the elements of the list"""
    # Base case
    if len(some_list) == 0:
        return
    #Recursive bits
    print(some_list[0])
    list_printer(some_list[1:])

my_list = [1, 2, 3, 4, 5, 6]
list_printer(my_list)
