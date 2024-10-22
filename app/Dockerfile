# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение в контейнер
COPY . .

# Открываем порт для приложения
EXPOSE 8000

# Запускаем приложение с uvicorn
ENTRYPOINT ["gunicorn"]
CMD ["-b", "0.0.0.0:8000", "-w", "4", "-k", "uvicorn.workers.UvicornH11Worker", "main:app"]
