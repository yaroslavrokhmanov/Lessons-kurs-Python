from mysql.connector import connect, Error
from tabulate import tabulate
try:
    connection = connect(
        host='localhost',
        user='root',
        password='',
        database='test',
        port=3307 
    )

    cursor = connection.cursor(dictionary=True)
    
    # query = "SELECT * FROM users WHERE age > 25"
    # cursor.execute(query)
    # result = cursor.fetchall()
    # print(tabulate(result))

# -  -----  --  ---
# 4  user4  30  900
# 5  user5  27  500
# 6  user6  28  500
# -  -----  --  ---

    query = "SELECT * FROM users WHERE age <= 30 AND salary > 500"
    cursor.execute(query)
    result = cursor.fetchall()
    print(tabulate(result)) 

# -  -----  --  ---
# 4  user4  30  900
# -  -----  --  ---

    cursor.close()
    connection.close()

except Error as e:
    print(e)
