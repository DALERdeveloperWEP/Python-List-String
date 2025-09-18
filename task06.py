text = "olol radar makka non"
result = []
for i in text.split(" "):
    if i == i[::-1]:result.append(i)

print(result)
