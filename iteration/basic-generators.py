def my_gen():
    print("Before 1")
    yield 1
    print("Between 1 & 2")
    yield 2
    print("Between 2 & 3")
    yield 3
    print("After 3")

for i in my_gen():
   print(i)

# Or we can interate over the object we get back when we call the generator
#g = my_gen()
# print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))