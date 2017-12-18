def counter(number):
    print(number)
    number = number + 1
    counter(number)

# This will crash!!!!!!
counter(1)