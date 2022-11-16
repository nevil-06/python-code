import json

sampleJson = {"key1": "value1", "key2": "value2","key3" : "value3"}

pytojson = json.dumps(sampleJson,indent=2,separators=(",","="))
print(pytojson)