tuple1 = (45, 45, 45, 45)
KEYCHECK = tuple1[0]
for item in tuple1:
    if item==KEYCHECK:
        flag=1
    else:
        break


if(flag==1):
    print("all are same")