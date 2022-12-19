# Реализация API для кинотеатра

Ваша задача – создать API, возвращающий список фильмов в формате, описанном в openapi-файле, и позволяющий получить информацию об одном фильме, а так же настроить запуск всех компонентов системы — Django, Nginx и Postgresql — с использованием docker-compose.

### Технологии
- Приложение запускается с помощью WSGI.
- Для отдачи статических файлов используется Nginx.
- Виртуализация осуществляется в Docker.
- Для взаимодействия между контейнерами используйте docker-compose.

## Запуск проекта в контейнере
Клонируйте репозиторий и перейдите в директорию django_api:
```
git clone https://github.com/Seniacat/new_admin_panel_sprint_2
cd new_admin_panel_sprint_2/django_api
```
Создайте и заполните .env файл с переменными окружения по примеру env.example:
```
echo DB_ENGINE=django.db.backends.postgresql >> .env

echo DB_NAME=postgres >> .env

echo POSTGRES_PASSWORD=postgres >> .env

echo POSTGRES_USER=postgres  >> .env

echo DB_HOST=db  >> .env

echo DB_PORT=5432  >> .env
```
Установите и запустите приложения в контейнерах командой:
```
docker-compose up -d
```
Создайте суперюзера для админки:
```
docker-compose exec -it django_app python manage.py createsuperuser
```

## API

Получение списка фильмов:
```
GET http://127.0.0.1/api/v1/movies/
```
Параметры запроса
- page - номер страницы списка фильмов.

Получение фильме по id:
```
GET http://127.0.0.1/api/v1/movies/{:filmwork_id}
```
Параметры запроса
- filmwork_id - id фильма;
- page - номер страницы списка фильмов.

Aдминка приложения:
```
http://127.0.0.1/admin/
```
