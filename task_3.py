import json
name_person = []
hobby_person = []
with open('users.csv', 'r', encoding="utf-8") as a, open('hobby.csv', 'r', encoding="utf-8") as b:
    name_person = a.read().splitlines()
    hobby_person = b.read().splitlines()

result = {}
for i in range(0, len(name_person)):
    if i <= len(hobby_person)-1:
        result[name_person[i]] = hobby_person[i]
    else:
        result[name_person[i]] = None
with open('result.csv', 'w', encoding="utf-8") as f:
    f.write(json.dumps(result, ensure_ascii=False))
    
print(result)
