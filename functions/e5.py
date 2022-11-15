def outFunc(a,b):
    result=0
    def inFunc(a,b):
         return a+b
    result=inFunc(a,b)
    return 5+result 
result1=outFunc(3,4)
print(result1)