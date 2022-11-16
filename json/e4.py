import json
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

sort_result = json.dumps(sampleJson,indent=2,sort_keys=True)

print(sort_result)