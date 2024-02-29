# Task tracker (REST API - тестовое задание)

Проект представляет собой backend приложения трекер задач


## Технологии:

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/) [![Django Rest Framework](https://img.shields.io/badge/-Django_Rest_Framework-092E20?style=flat)](https://www.django-rest-framework.org/)
[![Celery](https://img.shields.io/badge/-Celery-37814A?style=flat&logo=celery&logoColor=white)](http://www.celeryproject.org/)
[![Redis](https://img.shields.io/badge/-Redis-DC382D?style=flat&logo=redis&logoColor=white)](https://redis.io/)
[![API](https://img.shields.io/badge/-API-4CAF50?style=flat)](https://en.wikipedia.org/wiki/Application_programming_interface)
[![Swagger](https://img.shields.io/badge/-Swagger-85EA2D?style=flat&logo=swagger&logoColor=white)](https://swagger.io/)
[![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

## Описание:

В проекте представлены следующие модели:
- Исполнитель задачи
- Задача
- Проект

К одному проекту может быь привязано несколько задач, и одна и та же задача может быть в нескольких проектах.
Endpoints:
- task/update (Обновить задачу)
- task/create (Создать задачу)
- task/destroy (Удалить задачу)
- все дополнительные эндпоинты доступны для просмотра по ссылке ```http://localhost:8000/swagger/```

Реализована проверка всех задач раз в 24 часа, по истечению проверки просроченные задачи удаляются (посредством Celery).
При удалении задачи любым способом (Celery, админ панель, запрос) если на эту задачу назначен исполнитель, его счетчик удаленных задач должен увеличиваться на единицу, реализовано через сигналы.


## Установка:

- Для начала работы с проектом клонируйте репозиторий:
    - ```git clone https://github.com/NickolayBabulich/tracker.git```
- Произвести установку Docker (https://docs.docker.com/get-docker/)
- Перейдите в корневую директорию проекта
- Запустить проект командой ```docker compose up```
- Во время запуска проекта будут произведены следующие действия:
  - проведены миграции
  - создан суперпользователь
  - загружены тестовые-данные
  - запущен сервер

## Дополнительно:
- Для управления сущностями авторизуйтесь под администратором ```http://localhost:8000/admin/```
  - логин администратора: ```admin```
  - пароль администратора: ```1```
- Документация по эндпоинтам доступна по ссылке ```http://localhost:8000/swagger/```