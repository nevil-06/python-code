speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52,
         'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

new_space=list()

for item in speed.values():
    if item in new_space:
        continue
    else:
        new_space.append(item)

print(new_space)
