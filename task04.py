email = "ali@gmail.com,vali@mail.ru,karim@gmail.com"

result = []

for user in email.split(","):
    result.append(user[user.index("@"):])

print(result)