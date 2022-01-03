import json

json_string = '''[
  {
    "a": "this is a",
    "b": [1, 2,"熊猫"]
  },
  {
    "c": "thia is c"
  }
]'''

rs = json.loads(json_string)
json_string = json.dumps(rs, ensure_ascii=False)
print(json_string)

with open("data/test1.json", 'w', encoding='utf8') as fp:
    json.dump(rs, fp, ensure_ascii=False)
