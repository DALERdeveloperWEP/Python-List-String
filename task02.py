# Eski code 
# text = "Dasturlash, Sun'iy intellekt, Web dizayn" 
# l = text.split(" ")
# l2 = "_".join(l)
# l3 = l2.split(",")
# result = "".join(l3)
# print(result.lower())

# Yangilangan code
text = "Dasturlash, Sun'iy intellekt, Web dizayn" 
text_for = [p.strip().lower().replace(" ","_") for p in text.split(",")]
result = "_".join(text_for)
print(result)