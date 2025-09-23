email = "ali@gmail.com,vali@mail.ru,karim@gmail.com"

result = []

for user in email.split(","):
    if user[user.index("@"):] not in result:result.append(user[user.index("@"):])

print(result)