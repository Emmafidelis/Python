from pprint import pprint
sentence = "This is a common interview question"
unique = {}
for item in sentence:
    if item in unique:
        unique[item] += 1
    else:
        unique[item] = 1

unique_item = sorted(
    unique.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(unique_item)