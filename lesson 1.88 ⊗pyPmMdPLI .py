import matplotlib.pyplot as plt
import dateparser

# 1.Установите библиотеку matplotlib. Импортируйте ее в свой рабочий файл и протестируйте ее работу.

# matplotlib        3.10.1

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title("Wykres kwadratów liczb")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# 2.Установите библиотеку dateparser. Импортируйте ее в свой рабочий файл и протестируйте ее работу.

# dateparser        1.2.1

date = dateparser.parse("10 февраля 2024 года")
print(date) # 2024-02-10 00:00:00