''' odd even
I: create fun
P: loop through, print 1-2000, condition of odd n even
O: print 1 to 2000 with odd and  even
'''
# def odd_even():
#     for i in range(1, 2001):
#         if i%2 == 0:
#             print "Number is "+str(i)+". This is an even number."
#         else:
#             print "Number is "+str(i)+". This is an odd number."
#
# odd_even()

def multiply(arr1, num):
    new_list = []
    for i in arr1:
        new_list.append(i * num)
    return new_list

# arr1 = [2,4,10,16]
# b = multiply([2,4,5],3)
# print b

''' odd even
I: 1 arrays
P: multiply
O: list in list with 1 only, output form multiply function is [6, 12, 15]
==> [[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
'''
def layered_multiples(arr1): # arr1 = [6,12,15]
    # print arr1
    new_list1 = [] # is to keep track of list of 1's. ex. [1,1,1,1,1,1]
    # print new_list1
    new_array = [] # is to add the above at the right index. ex. [[1,1,1,1,1,1],....]
    # print new_list2
    for i in arr1: # is to add the number of 1s equivalent to the value at the index ex. arr1[0] = 6 so [1,1,1,1,1,1].
        new_list1 = []
        while i > 0:
            new_list1.append(1)
            i = i - 1
            # print new_list1
            # print new_list2
        new_array.append(new_list1)
        # print new_list1
        # print new_list2

    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x

''' odd even
I: num,
P:
O:
'''



''' odd even
I: num,
P:
O:
'''


''' odd even
I: num,
P:
O:
'''
