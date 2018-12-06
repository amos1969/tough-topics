def summer(number):
    """Takes a positive integer and recursively sums the integers up to 
    it, returning the sum of them all."""
    #Base case
    if number < 1:
        return 0
    # Recursive call
    return number + summer(number-1)

# Should output 5050
print(summer(100))