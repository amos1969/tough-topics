def factorial(number):
    # Base Case
    if number <= 1:
        return 1
    # Not the Base Case
    return number * factorial(number - 1)

print(factorial(997)) 