# 2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.
#
# import numpy as np
# random_array = np.random.rand(5) # массив из 5 случайных чисел
# print(random_array)
#
import matplotlib.pyplot as plt
import numpy as np

random_array_x = np.random.rand(50) # массив x из 50 случайных чисел
random_array_y = np.random.rand(50) # массив y из 50 случайных чисел

# Строим диаграмму рассеяния:
plt.scatter(random_array_x, random_array_y)

# Кастомизируем график:
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Тестовая диаграмма рассеяния")

# Показываем график:
plt.show()