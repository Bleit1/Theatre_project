FROM python:3.10-slim

LABEL maintainer="arseniyaristov07@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app


# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home django-user && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol/web/

USER django-user

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
