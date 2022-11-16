set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
for item1 in set1:
    for item2 in set2:
        if item1==item2:
            print("yes common element is preesne")
            final_set=set1.intersection(set2)
print(final_set)