# 1. Создай гистограмму для случайных данных,
# сгенерированных с помощью функции `numpy.random.normal`
# Параметры нормального распределения
#
# mean = 0 # Среднее значение
# std_dev = 1 # Стандартное отклонение
# num_samples = 1000 # Количество образцов
# # Генерация случайных чисел, распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)
#
import matplotlib.pyplot as plt
import numpy as np

mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
num_samples = 1000  # Количество образцов
# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=20, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Показать гистограмму
plt.show()