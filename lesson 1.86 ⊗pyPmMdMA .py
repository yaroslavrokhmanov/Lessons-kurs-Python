from custom_math import *
from user import *

# 1.Импортируйте все функции из модуля custom_math, созданного вами в предыдущем уроке.
get_divide(100, 5) # 20.0

# 2.Модифицируйте предыдущую задачу так, чтобы функция get_divide не могла импортироваться вместе со всем содержимым модуля.
get_divide(100, 5) # Rezultat tot rze 20.0 chotia pered funkcijej podczerkiwanie:
#  def _get_divide(num1, num2):
#     print(num1 / num2)

# 3.Сделайте недоступными для импорта пароль и почту пользователя из модуля user.
print(password) # NameError: name 'password' is not defined