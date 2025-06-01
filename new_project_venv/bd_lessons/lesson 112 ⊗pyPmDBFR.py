from mysql.connector import connect, Error
from tabulate import tabulate

# 1. Переименуйте поле зарплаты юзеров при выводе их в консоль.
# 2. Выведите имя, возраст и зарплату юзеров, при этом переименуйте их имена и возраст.
try:
    connection = connect(
        host='localhost',
        user='root',
        password='',
        database='test',
        port=3307 
    )
    
    cursor = connection.cursor(dictionary=True)

# 1. Переименуйте поле зарплаты юзеров при выводе их в консоль.
    query = "SELECT salary AS money FROM users"

    cursor.execute(query)
    result = cursor.fetchall()
    print(tabulate(result, headers="keys"))

    print("OK")

    cursor.close()
    connection.close()
#   money
# -------
#     400
#     500
#     900
#     500

# 2. Выведите имя, возраст и зарплату юзеров, при этом переименуйте их имена и возраст.
    query = "SELECT name AS users_name, age AS users_age FROM users"

    cursor.execute(query)
    result = cursor.fetchall()
    print(tabulate(result, headers="keys"))

    print("OK")

    cursor.close()
    connection.close()

# users_name      users_age
# ------------  -----------
# user1                  23
# user2                  25
# user3                  23
# user4                  30
# user5                  27
# user6                  28

except Error as e:
    print("Mistake")
