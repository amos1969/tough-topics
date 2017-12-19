my_list = ["One", "Two", "Three"]

# for item in my_list:
#     print(item)

itr = my_list.__iter__()
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))