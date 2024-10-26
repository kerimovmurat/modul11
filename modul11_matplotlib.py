import matplotlib.pyplot as plt

# Пример данных
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание графика
plt.plot(x, y, marker='o')
plt.title('Пример графика')
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.grid()

# Сохранение графика
plt.savefig('plot.png')
plt.show()
