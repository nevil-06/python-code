s1 = "Yn"
s2 = "PYnative"
def present(s1,s2):
    flag=0
    for i in s1:
        if i in s2:
            continue
        else:
            flag = False
    return flag
result=present(s1,s2)
print("blanced string",result)
