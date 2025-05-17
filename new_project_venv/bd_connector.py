from mysql.connector import connect, Error

try:
    # Создаем подключение вручную
    connection = connect(
        host='localhost',
        user='root',
        password='',
        database='test',
        port=3307 
    )

    # Создаем курсор и выполняем запрос
    cursor = connection.cursor(dictionary=True)
    
    # Выполнение запроса
    query = "SELECT * FROM users WHERE age > 25"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    # Еще один запрос
    query = "SELECT * FROM users WHERE age < 30 AND salary > 500"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

    # Закрываем курсор и соединение
    cursor.close()
    connection.close()

except Error as e:
    print(e)
