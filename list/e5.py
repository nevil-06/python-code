list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
final_pro = zip(list1[0::],list2[::-1])
print(tuple(final_pro))