import json
data = {"key1" : "value1", "key2" : "value2"}
print(data)
json_convert = json.dumps(data,indent=2)
print(json_convert)
