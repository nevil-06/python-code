sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
result = dict()
for i in sample_list:
    if i in sample_list:
        result[i]+=1
    else:
        result[i]=1


print(result)