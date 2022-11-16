import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

jsonto_python = json.loads(sampleJson)
print(jsonto_python['key2'])