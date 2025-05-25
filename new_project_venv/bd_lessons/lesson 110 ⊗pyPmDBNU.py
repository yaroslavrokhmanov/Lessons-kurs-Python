from mysql.connector import connect, Error
from tabulate import tabulate

# 1.Используя созданный ранее вами дамп таблицы users приведите ее в исходное состояние.
# 2.Юзеру с id 4 поставьте возраст 35 лет.
# 3.Всем, у кого зарплата 500, сделайте ее 700.
# 4.Работникам с id больше 2 и меньше 5 включительно поставьте возраст 23.

try:
    connection = connect(
        host='localhost',
        user='root',
        password='',
        database='test',
        port=3307 
    )
    
    cursor = connection.cursor(dictionary=True)

    # 2.Юзеру с id 4 поставьте возраст 35 лет.
    cursor.execute("UPDATE users SET age=27 WHERE id=5")

    #   id  name      age    salary
# ----  ------  -----  --------
#    1  user1      23       400
#    2  user2      25       500
#    3  user3      23       500
#    4  user4      35       900
#    5  user5      27       500
#    6  user6      28       900

    # 3.Всем, у кого зарплата 500, сделайте ее 700.

    cursor.execute("UPDATE users SET salary=700 WHERE salary=500")

#      id  name      age    salary
# ----  ------  -----  --------
#    1  user1      23       400
#    2  user2      25       700
#    3  user3      23       700
#    4  user4      35       900
#    5  user5      27       700
#    6  user6      28       900

# Работникам с id больше 2 и меньше 5 включительно поставьте возраст 23.
    cursor.execute("UPDATE users SET age = 23 WHERE id > 2 AND id <= 5")

#       id  name      age    salary
# ----  ------  -----  --------
#    1  user1      23       400
#    2  user2      25       700
#    3  user3      23       700
#    4  user4      23       900
#    5  user5      23       700
#    6  user6      28       900

    connection.commit()
    print("OK")

    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    print(tabulate(result, headers="keys"))

    cursor.close()
    connection.close()

#   id  name      age    salary
# ----  ------  -----  --------
#    1  user1      23       400
#    2  user2      25       500
#    3  user3      23       500
#    4  user4      35       900
#    5  user5      27       500
#    6  user6      28       900



except Error as e:
    print("Mistake")
