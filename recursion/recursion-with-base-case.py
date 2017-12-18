def counter(number):
    if number > 100:
        return
    print(number)
    number = number + 1
    counter(number)

# This will crash!!!!!!
counter(1)