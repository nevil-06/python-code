s1 = "Abc"
s2 = "Xyz"

sFirst =s1[0]+s2[-1]
sMiddle =s1[len(s1)//2]+s2[len(s2)//2]
sLast = s1[-1]+s2[0]
print(sFirst+sMiddle+sLast)