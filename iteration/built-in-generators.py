import itertools
import time

itr = itertools.count()
while True:
    print(next(itr))
    time.sleep(0.5)

# itr2 = itertools.product([1, 2, 3], [1, 2, 3])
# for item in itr2:
#     print(item)