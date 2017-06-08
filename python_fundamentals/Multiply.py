def Multiply(arr,num):
    # print arr, num
    # arr_new = []
    for x in range(len(arr)):
        # print x
        arr[x] *= num
        # print arr
    return arr
    #     y = x
    #     arr_new.append(y)
    # return arr_new
a = [2,4,10,16]
b = Multiply(a,5)
print b
