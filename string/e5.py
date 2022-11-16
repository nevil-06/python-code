str1 = "PyNaTive"

def spilt(str1):
    lower = []
    upper= []
    for i in str1:
        if i.islower():
            lower.append(i)
        else:
            upper.append(i)
    result= ''.join(lower+upper)
    return result

result = spilt(str1)
print(result)
