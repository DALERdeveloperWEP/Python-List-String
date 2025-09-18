bio = "Ism:Ali, Familiya:Valiyev, Yil:2002"
for i in bio.split(", "):
    key, value = i.split(":")
    print(f"{key}: {value}")
    