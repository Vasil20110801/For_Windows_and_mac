import json
lst = ["vasil","gosho","ivan"]

with open("01json.json", "w") as f:
    json.dump(lst,f)

with open("01json.json", "r") as f1:
    print(f1.read())