#1st approach
str = "James"
newstring = str[0:5:2]
print(newstring)


#2nd approach
str = "James"
sFirst = str[0]
sMiddle = str[(len(str)//2)]
sLast=str[-1]
print(sFirst+sMiddle+sLast)