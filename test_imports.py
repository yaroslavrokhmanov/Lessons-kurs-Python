try:
    import jsonobject
    print("✅ jsonobject импортирован успешно")
except ImportError as e:
    print("❌ Ошибка при импорте jsonobject:", e)

try:
    from tabulate import tabulate
    print("✅ tabulate импортирован успешно")
except ImportError as e:
    print("❌ Ошибка при импорте tabulate:", e)

try:
    import matplotlib.pyplot as plt
    print("✅ matplotlib импортирован успешно")
except ImportError as e:
    print("❌ Ошибка при импорте matplotlib:", e)

try:
    import dateparser
    print("✅ dateparser импортирован успешно")
except ImportError as e:
    print("❌ Ошибка при импорте dateparser:", e)

try:
    import numpy as np
    print("✅ numpy импортирован успешно")
except ImportError as e:
    print("❌ Ошибка при импорте numpy:", e)
