from mysql.connector import connect, Error
from tabulate import tabulate

# 1.Добавьте нового юзера 'xxxx', не указав ему возраст и зарплату.

try:
    connection = connect(
        host='localhost',
        user='root',
        password='',
        database='test',
        port=3307 
    )

    cursor = connection.cursor(dictionary=True)
    
    query = "INSERT INTO users(name) VALUES ('xxxx')"
    cursor.execute(query)
    connection.commit()
    print("Add information")

    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    print(tabulate(result, headers="keys"))

    cursor.close()
    connection.close()

except Error as e:
    print("Mistake")

#   id  name      age    salary
# ----  ------  -----  --------
#    1  user1      23       400
#    2  user2      25       500
#    3  user3      23       500
#    4  user4      30       900
#    5  user5      27       500
#    6  user6      28       500
#    9  user       30      1000
#   10  user7      26       300
#   11  user8      32      1100
#   12  user9      22       350
#   13  xxxx        0         0