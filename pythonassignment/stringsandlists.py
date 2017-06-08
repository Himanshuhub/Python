str = "It's thanksgiving day. It's my birthday,too!"
print str.find("day")
newString = str.replace("day","month",1)
print newString

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]
y =[]
y.append(x[0])
y.append(x[len(x)-1])
print y

x = [19,2,54,-2,7,12,98,32,10,-3,6]
y =[]
x.sort()
breakPoint = len(x)/2
y.append(x[:breakPoint])
for count in range(breakPoint,len(x)):
    y.append(x[count])

print y
