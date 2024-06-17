import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from time import perf_counter
import pandas as pd
# Создание 2 массивов
a = np.random.rand(1000000)
b = np.random.rand(1000000)
t_start = perf_counter()
result = np.multiply(a, b) # перемножение
t_end = perf_counter()
print("Execution time:", t_end - t_start, "seconds")

df = pd.read_csv('7\Lab-7\data1.csv',delimiter=';')


# Выделение данных
data_1_4 = df.iloc[:, [0, 3]]  # столбцы 1 и 4
data_1_10 = df.iloc[:, [0, 9]]  # столбцы 1 и 10

# Построение графиков
plt.figure(figsize=(10, 5))

# Первый график (столбцы 1 и 4)
plt.plot(data_1_4.iloc[:, 0], data_1_4.iloc[:, 1], label='Столбцы 1 и 4')

# Второй график (столбцы 1 и 10)
plt.plot(data_1_10.iloc[:, 0], data_1_10.iloc[:, 1], label='Столбцы 1 и 10')

# Настройка легенды
plt.legend()

# Показать график
plt.show()

# График корреляции
plt.figure(figsize=(10, 5))
plt.scatter(data_1_4.iloc[:, 1], data_1_10.iloc[:, 1])
plt.title('График корреляции между столбцами 4 и 10')
plt.xlabel('Столбец 4')
plt.ylabel('Столбец 10')
plt.show()

#3================================
# создаем и вычисляем координаты
x = np.linspace(-10, 10, num=50)
y = np.linspace(-0.5, 0.5, num=50)
X, Y = np.meshgrid(x, y)
Z = np.tanh(np.sqrt(X**2 + Y**2))

# создаем 3d анимацию,используя Axes3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, antialiased=True)
plt.show()