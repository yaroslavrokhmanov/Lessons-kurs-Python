from mysql.connector import connect, Error
from tabulate import tabulate

# 1.Достаньте юзеров, у которых зарплата имеет значения 400 и 900.
# 2.Достаньте юзеров, возраст которых составляет 25, 27 и 28 лет. При этом id более 2.

try:
    connection = connect(
        host='localhost',
        user='root',
        password='',
        database='test',
        port=3307 
    )
    
    cursor = connection.cursor(dictionary=True)

# 1.
    query = "SELECT * FROM users WHERE salary IN (400, 900)"

    cursor.execute(query)
    result = cursor.fetchall()

    print(tabulate(result, headers="keys"))

    cursor.close()
    connection.close()
    except Error as e:
    print("Mistake")

#   id  name      age    salary
# ----  ------  -----  --------
#    1  user1      23       400
#    4  user4      30       900
# 2.
    query = "SELECT * FROM users WHERE age IN (25, 27, 28) AND id > 2"

      cursor.execute(query)
    result = cursor.fetchall()

    print(tabulate(result, headers="keys"))

except Error as e:
    print("Mistake")

#   id  name      age    salary
# ----  ------  -----  --------
#    5  user5      27       500
#    6  user6      28       500
