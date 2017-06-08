# Fun with functions
import random

# Odd Even
# def odd_even():
#     for i in range(0,2001,1):
#         if (i%2==0):
#             print "Number id "+str(i)+". This is an even number."
#         else:
#             print "Number id "+str(i)+". This is an odd number."
#
# odd_even()

# Multiply
def Multiply(l,mult):
    for i in range(len(l)):
        l[i] = l[i] * mult
    print l
    return l

# Multiply([2,4,10,16], 5)

# Hacker Challenge:
def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array
#
x = layered_multiples(Multiply([2,4,5],3))
# # putput would be [6,12,15] form Multiply function will be passed on as argument
print x
#     return new_array

# layered_multiples([2,4,5])
