sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keysToUse = ["name", "salary"]

new_dict = dict()
for item in keysToUse:
    if item in sample_dict:
        new_dict.update({item:sample_dict[item]})

print(new_dict)