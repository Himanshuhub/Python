l = ['hello','world','my','name','is','Anna']
char = 'o'
newlist =[]
for mystring in l:
    if mystring.find(char) > -1:
        newlist.append(mystring)
print newlist        
