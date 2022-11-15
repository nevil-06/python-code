list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list_new = []

for i in range(len(list1)):
    if(list1[i]%2!=0):
        list_new.append(list1[i])

for i in range(len(list2)):
    if(list1[i]%2==0):
        list_new.append(list2[i])

print(list_new)

#done