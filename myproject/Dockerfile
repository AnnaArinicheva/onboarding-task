FROM python:3.8

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование файла зависимостей и установка зависимостей
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего проекта в рабочую директорию
COPY . /app/

# Открытие порта, который будет слушать приложение
EXPOSE 8000

# Команда для запуска приложения
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000

