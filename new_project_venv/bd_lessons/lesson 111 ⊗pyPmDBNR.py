from mysql.connector import connect, Error
from tabulate import tabulate

# 1.Удалите юзера с id, равным 7.
# 2.Удалите всех юзеров, у которых возраст 23 года.
# 3.Удалите всех юзеров, у которых id больше 5 и зарплата больше или равна 900.
# 4.Работникам с id больше 2 и меньше 5 включительно поставьте возраст 23.
# 5.Удалите всех юзеров.

try:
    connection = connect(
        host='localhost',
        user='root',
        password='',
        database='test',
        port=3307 
    )
    
    cursor = connection.cursor(dictionary=True)
# 1.Удалите юзера с id, равным 7.
    # cursor.execute("INSERT INTO users (name, age, salary) VALUES ('user7', 98, 300)")
    cursor.execute("DELETE FROM users WHERE ID = 7")

# 2.Удалите всех юзеров, у которых возраст 23 года.
    cursor.execute("DELETE FROM users WHERE age = 23")
#   id  name      age    salary
# ----  ------  -----  --------
#    2  user2      25       700
#   15  user6      28       900
#   16  user7      98       300

# 3.Удалите всех юзеров, у которых id больше 5 и зарплата больше или равна 900.
    cursor.execute("DELETE FROM users WHERE id > 5 AND salary >= 900")
#   id  name      age    salary
# ----  ------  -----  --------
#    2  user2      25       700
#   16  user7      98       300

# 4.Работникам с id больше 2 и меньше 5 включительно поставьте возраст 23.
    cursor.execute("UPDATE users SET age = 23 WHERE id > 2 AND id <= 5")

# 5.Удалите всех юзеров.
    cursor.execute("DELETE FROM users") 
    cursor.execute("ALTER TABLE users AUTO_INCREMENT = 1")

    connection.commit()
    print("OK")

    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    print(tabulate(result, headers="keys"))

    cursor.close()
    connection.close()



except Error as e:
    print("Mistake")
