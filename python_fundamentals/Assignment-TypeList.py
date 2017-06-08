'''
#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The array you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"
'''
# l = ['magical unicorns',19,'hello',98.98,'world']
# l = [2,3,1,7,4,12]
l = ['magical','unicorns']

def TypeList(l):
    newString = ""
    my_sum = 0
    decisionstring = 0
    decisionint = 0
    for i in l:
        if isinstance(i,str):
            newString += i+ " "
            decisionstring += 1
        elif isinstance(i,int):
            my_sum += i
            decisionint += 1
        elif isinstance(i,float):
            my_sum += i
            decisionint += 1
    if (decisionstring>0 and decisionint==0):
        print "The array you entered is of string type"
        print "String: " +newString

    if (decisionstring==0 and decisionint>0):
        print "The array you entered is of int type"
        print "Sum: " +str(my_sum)

    if (decisionstring>0 and decisionint>0):
        print "The array you entered is of mixed type"
        print "String: " +newString
        print "Sum: " +str(my_sum)

TypeList(l)
