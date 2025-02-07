# Используйте официальный образ Python версии 3.11
FROM python:3.11-slim

# Установите рабочую директорию в контейнере
WORKDIR /app

# Скопируйте файлы проекта в рабочую директорию
COPY . /app

# Установите зависимости из файла requirements.txt без кэширования для минимизации размера образа
RUN pip3 install --no-cache-dir -r requirements.txt

# Запустите вашего бота при старте контейнера
CMD ["python3", "bot.py"]