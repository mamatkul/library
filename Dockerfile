# Используем базовый образ Python
FROM python:alpine

# Устанавливаем переменную окружения для отключения буферизации вывода
ENV PYTHONUNBUFFERED 1

# Создаем директорию приложения внутри контейнера
WORKDIR /app

# Устанавливаем зависимости проекта
COPY requirements.txt /app/
RUN apk add --no-cache build-base postgresql-dev musl-dev
RUN pip install -r requirements.txt

# Копируем файлы проекта внутрь контейнера
COPY . /app/

# Определяем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
