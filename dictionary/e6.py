sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]


sample_dict.pop("name")
sample_dict.pop("salary")

print(sample_dict)