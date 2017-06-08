'''
def add(a,b):
    x = a + b
    return x
# result = add(3,5)
print (add(3,5))

print (add(1,2))
'''
'''
def say_hi(name):
    print "Hi " + name

say_hi("Himanshu")
'''
# name is a parameter
# himanshu is an argument

# def say_hi():
#     return "Hi"
#     greeting = say_hi()
#     print greeting
#     print "Hi " + name
#
# say_hi("Himanshu")
'''
def add(a,b):
    x = a+b
    print x
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
print sum3

def multiply(arr, num):
    def multiply(arr,num):
    for x in arr:
        x *= num
    return arr


a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[2,4,10,16]
'''

'''
def multiply(arr, num):
    # print arr, num
    for x in range(len(arr)):
        # print x
        arr[x] *= num
        # print arr
    return arr

a = [2,4,10,16]
b = multiply(a,5)
print b
'''
'''
tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1,2,3,4,5)
tuple_letters = "a", "b", "c", "d"
print tuple_data, tuple_num, tuple_letters
'''
dog = ("Canis Familiaris", "dog", "carnivore", 12)
# print dog[2]
# for i in dog:
#     print i
dog = dog + ('domestic',)
# print dog

dog = dog[:3] + ("man's best friend",) + dog[4:]
print dog
