first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
third_set = set()
for i in first_set:
    if i in second_set:
        third_set.add(i)

print(third_set)
final_set = first_set-third_set
print(final_set)