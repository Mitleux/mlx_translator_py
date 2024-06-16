import json

str1 = '{"qwer": "rty","qwerty": "yui"}'
str2 = 'qwer'
json1 = json.loads(str1, strict=False)

print(str1)
print(json1['qwer'][0][0])
