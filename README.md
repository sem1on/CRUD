# Задание

Сделайте CRUD для юзеров с токен аутентификацией. 
Для примера можно взять https://emphasoft-test-assignment.herokuapp.com/swagger/

Для запуска приложения:
1) cd/путь_до_проекта
2) создать Superuser
3) запустить сервер: python manage.py runserver

Создание пользователей через Admin или в БД

Примеры запросов через Postman: 
1) POST  http://127.0.0.1:8000/api-token-auth/token/login    Присвоение токена существующему пользователю  { "username": "user1", "password": "1234" } 
2) POST  http://127.0.0.1:8000/api/v1/users/                 Добавление пользователя                       { "username": "user2", "password": "1234" }
3) GET   http://127.0.0.1:8000/api/v1/users/{id}/            Просмотр всех пользователей                   Content-Type: application/json 
4) PUT   http://127.0.0.1:8000/api/v1/users/{id}/            Редактирование пользователя                   { "last_name": "LastName" } 
5) PATCH http://127.0.0.1:8000/api/v1/users/{id}/            Редактирование пользователя                   { "first_name": "FirstName" } 
6) DELET http://127.0.0.1:8000/api/v1/users/{id}/            Удаление пользователя 
