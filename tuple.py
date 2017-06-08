'''
value = ("Michael", "Instructor", "Coding Dojo")
print value
# Tuple assognment
(name, position, company) = value
print name
print position
print company
'''
# tuple_data = ('physics', 'chemistry', 1997, 2000)
# print len(tuple_data)

tuple_data = ('physics', 'chemistry', 'x-ray', 'python', 'zzz', False, 0, None)
tuple_num = (67, 89, 31, 15)
# print max(tuple_data)
# print min(tuple_data)
# print min(tuple_num)
# print sum(tuple_num)
# print all(tuple_data)
# print any(tuple_num)

# num = (1,5,7,3,8)
# for index, item in enumerate(num):
#     print(str(index)+ "="+str(item))

num = (1,5,7,3,8)
# print sorted(num)

# print tuple(reversed(num))

# print list(reversed(num))

# print list = tuple(reversed(num))

def get_circle_area(r):
    c = 2 * 3.14 * r
    a = 3.14 * r * r
    print c, a
    return(c,a)

get_circle_area(5)
# print value
