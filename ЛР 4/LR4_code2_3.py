"""Задание 3 комплект 2"""

import matplotlib.pyplot as plt
import numpy as np


"""Создание первого окна с двумя графиками двух функций"""
plt.figure(1)
x = np.linspace(-10, 10, 400) # создание массива х
y = 2 * x + 3
a = 1; b = 0; c = 0
y1 = a * x**2 + b * x + c

plt.subplot(2, 1, 1) # создает количество строк, количество столбцов, номер текущего подграфика
plt.plot(x, y, color = 'blue', label = 'y = kx + b') # построение графика
plt.title('График прямой')
plt.xlabel('Ox') # подпись осей
plt.ylabel('Oy')
plt.axhline(0, color='black', linewidth = 0.5, ls='--') # добавление осей координат
plt.axvline(0, color='black', linewidth = 0.5, ls='--')
plt.grid() # отображение сетки
plt.legend() # отображение легенды

plt.subplot(2, 1, 2)
plt.plot(x, y1, color = 'red', label = 'y = ax**2 + bx + c')
plt.title('График параболы')
plt.xlabel('Ox')
plt.ylabel('Oy')
plt.axhline(0, color='black', linewidth = 0.5, ls='--')
plt.axvline(0, color='black', linewidth = 0.5, ls='--')
plt.grid()
plt.legend()


"""Создание второго окна с одним графиком"""
plt.figure(2)
y2 = np.tan(x)
plt.plot(x, y2, color = 'green', label = 'tan(x)')
plt.title('График тангенса')
plt.xlabel('Ox')
plt.ylabel('Oy')
plt.axhline(0, color='black', linewidth = 0.5, ls='--')
plt.axvline(0, color='black', linewidth = 0.5, ls='--')
plt.grid()
plt.legend()


plt.tight_layout() # автоматическая настройка расположения подграфиков
plt.show()