my_list = ["David", "Michael", "Steve", "Simon", "Kirstin", "Luke", "Emma", "Matthew",
           "Lorna", "Michael", "Anne", "Mark", "James", "Iain", ]

#for name in my_list:
#    print(name)

itr = my_list.__iter__()
while True:
    try:
        print(next(itr))
    except StopIteration:
        break