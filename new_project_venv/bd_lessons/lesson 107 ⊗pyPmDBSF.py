from mysql.connector import connect, Error
from tabulate import tabulate

# 1.Выберите из таблицы users имя, возраст и зарплату для каждого работника.
# 2.Выберите id, name и age юзеров, зарплата которых больше 400, но меньше 900.

try:
    connection = connect(
        host='localhost',
        user='root',
        password='',
        database='test',
        port=3307 
    )

    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT name, age, salary FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    print(tabulate(result)) 

# user1  23  400
# user2  25  500
# user3  23  500
# user4  30  900
# user5  27  500
# user6  28  500

    query = "SELECT id, name, age FROM users WHERE salary > 400 AND salary < 900"
    cursor.execute(query)
    result = cursor.fetchall()
    print(tabulate(result)) 

# 2  user2  25
# 3  user3  23
# 5  user5  27
# 6  user6  28

    cursor.close()
    connection.close()

except Error as e:
    print(e)
