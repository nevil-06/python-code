list_1 = [3, 6, 9, 12, 15, 18, 21]
list_2 = [4, 8, 12, 16, 20, 24, 28]
list_3 = list()
for i in range(len(list_1)):
    if i%2!=0:
        list_3.append(list_1[i])

for i in range(len(list_2)):
    if i%2==0:
        list_3.append(list_2[i])

print(list_3)
