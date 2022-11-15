def recur(num):
    result=0
    if num<=1:
        return num
    return num+recur(num-1)
result1=recur(10)
print(result1)