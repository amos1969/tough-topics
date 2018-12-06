def digit_sum(number):
    """ Takes a number as a parameter which is assumed to 
    be an integer and positive"""
    # Base case
    if number < 10:
        return number
    # Gives us the last digit
    digit = number % 10
    # Gives us the number with the last digit removed
    new_number = number // 10
    # Recursive call
    return digit + digit_sum(new_number)

# Should be 9
print(digit_sum(234))

# Should be 45
print(digit_sum(123456789))

# Should be 7
print(digit_sum(7))