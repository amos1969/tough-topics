def crasher(number):
    number = number + 1
    print(number)
    if number >= 100:
        return
    else:
        crasher(number)

crasher(1)