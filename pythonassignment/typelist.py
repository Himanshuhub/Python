l = ['magical unicorns',19,'hello',98.98,'world']
newString =""
my_sum =0
decisionfloat =0
# decissionnumber =0
decisionstring = 0
decisionint = 0
for i in l:
    if isinstance(i,str):
        newString+= i+" "
        decisionstring += 1
    elif isinstance(i,int):
        my_sum+= i
        decisionint += 1
    elif isinstance(i,float):
        my_sum+= i
        decisionfloat+=1
print newString,my_sum        
if (decisionstring > 0 and decisionint == 0):
    print "The array you entered is of String type"
elif (decisionint > 0 and decisionstring == 0):
    print "The array you entered is of int type"
elif (decisionfloat > 0 and decisionint ==0):
    print "The array you entered is of float type"
elif (decisionstring>0 and decisionint > 0):
    print "The array you entered is of mixed type"
elif (decisionfloat>0 and decisionint > 0):
    print "The array you entered is of mixed type"
