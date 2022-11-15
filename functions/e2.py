def varArg(*num):
    for i in range(len(num)):
        print(num[i],end=" ")

varArg(10,20,30)

varArg(80,100)