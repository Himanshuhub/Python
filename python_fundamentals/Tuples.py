import math

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1,2,3,4,5)
tuple_letters = "a", "b", "c", "d"
dog = ("Canis Familiaris", "dog", "carnivore", 12, "Domestic")

# print dog[2]

# for i in dog:
#     print i

# dog[0] = "X"

# dog = dog + ("Domestic",)
# print dog

# dog = dog[:4] + ("man's best friend",) + dog[4:]
# print dog

x = (1,5,6,9,2)
# print len(x)
# print max(x)
# print sum(x)
# print enumerate([1,2])
# print min(x)
# print sorted(x)

def get_circle_area(r):
    c = 2 * math.pi * r
    a = math.pi * r * r
    print (c,a)
    return (c,a)
get_circle_area(3)
