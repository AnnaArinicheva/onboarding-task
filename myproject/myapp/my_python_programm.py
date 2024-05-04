import numpy as np
import matplotlib.pyplot as plt
import os

def create_plot(a):
    # Преобразование ввода в float
    try:
        a = float(a)
    except ValueError:
        # В случае ошибки преобразования, можно задать a значение по умолчанию или обработать ошибку
        a = 1.0  # Например, устанавливаем значение по умолчанию
        
    # Генерация данных
    x = np.linspace(0, 10, 100)
    y = a*np.sin(x)

    # Создание графика
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='sin(x)')
    plt.title("График функции a*sin(x)")
    plt.xlabel("x")
    plt.ylabel("a*sin(x)")
    plt.legend()
    plt.grid(True)

    path = os.path.join('myapp/static/images', 'myplot.png')
    plt.savefig(path)
    plt.close()

    return '/static/images/myplot.png'

