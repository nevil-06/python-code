def newStr(s1,s2):
    sFirst = s1[0]+s2[0]
    sMiddle = s1[(len(s1)//2)]+s2[(len(s2)//2)]
    sLast=s1[-1]+s2[-1]
    return sFirst+sMiddle+sLast 

s1 = "America"
s2 = "Japan"
result=newStr(s1,s2)
print(result)

