from mysql.connector import connect, Error
from tabulate import tabulate

# 1.Добавьте нового юзера 'user7', 26 лет, зарплата 300.
# 2.Добавьте нового юзера 'user8', 32 лет, зарплата 1100.
# 3.Добавьте нового юзера 'user9', 22 лет, зарплата 350.
try:
    connection = connect(
        host='localhost',
        user='root',
        password='',
        database='test',
        port=3307 
    )

    cursor = connection.cursor(dictionary=True)
    
    query = "INSERT INTO users(name, age, salary) VALUES ('user7', 26, 300)"
    cursor.execute(query)
    connection.commit()
    print("Add information 1")

    query = "INSERT INTO users(name, age, salary) VALUES ('user8', 32, 1100)"
    cursor.execute(query)
    connection.commit()
    print("Add information 2")

    query = "INSERT INTO users(name, age, salary) VALUES ('user9', 22, 350)"
    cursor.execute(query)
    connection.commit()
    print("Add information 3")

    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    print(tabulate(result, headers="keys"))

    cursor.close()
    connection.close()

except Error as e:
    print("Mistake")

# Add information
# Add information
# Add information

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
#   14  user9      22       350

