# Integer
def FilterByType(arg):
    if isinstance(arg, int):
        if arg >= 100:
            print "that's a big number"
        else:
            print "That's a small number"

    elif isinstance(arg, str):
        if len(arg) >= 50:
            print "Long sentence"
        else:
            print "Short sentence"

    elif isinstance(arg, list):
        if len(arg) >= 10:
            print "Big list!"
        else:
            print "Short list"
    else:
        print "incorrect input"

# print FilterByType([1,1,1,1,1,1,1,1,1,1,1,1,"Q"])
# print FilterByType([1,1,1,1,1,1,1,1,1,1,1,1,"Q"])
# print FilterByType([1,1,1,1,1,1,1,1,1,1,1,1,"Q"])
# print FilterByType([1,1,1,1,1,1,1,1,1,1,1,1,"Q"])
# print FilterByType("1,1,1,1,1,1,1,1,1,1,1,1,Q")
print FilterByType("hi how r u. I think you should work more focused and more hours")
