def integer_sum(number):
    if number < 10:
        return number
    quotient = number // 10
    remainder = number % 10
    return remainder + integer_sum(quotient)


print(integer_sum(2018))