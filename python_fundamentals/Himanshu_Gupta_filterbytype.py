def filterbytype(arg):
    if isinstance(arg,int):
        if arg<100:
            print "That's a small number"
        elif arg>= 100:
            print "That's a big number!"
    elif isinstance(arg,str):
        if len(arg)<50:
            print "Short sentence."
        elif len(arg)>= 50:
            print "Long sentence."
    elif isinstance(arg,list):
        if len(arg)>=10:
            print "Big List!!"
        elif len(arg)< 10:
            print "Short List."
    else:
        print "incorrect input"



# print filterbytype(-23)


print filterbytype("hi how r u. I think you should work more focused and more hours")
