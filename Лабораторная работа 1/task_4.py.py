users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

def solve():
    visits = dict()
    for user in users:
        if user not in visits:
            visits[user] = 1
        else:
            visits[user] += 1
    unique = dict()
    unique["Общее количество"] = len(users)
    unique["Уникальные посещения"] = len(visits)
    return unique
print(solve())