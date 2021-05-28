import json
f=open("data.json")
data=json.load(f)
for i in data["colors"]:
    print(i)
f.close

