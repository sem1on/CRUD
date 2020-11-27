# Тестовое задание

Сделайте CRUD для юзеров с токен аутентификацией. 
Для примера можно взять https://emphasoft-test-assignment.herokuapp.com/swagger/

Для запуска приложения:
1) cd/путь_до_проекта
2) создать Superuser
3) запустить сервер: python manage.py runserver

Примеры запросов через Postman: 
1) POST http://127.0.0.1:8000/api-token-auth/ { "username": "user1", "password": "1234" } 
2) POST http://127.0.0.1:8000/api/v1/users/ { "username": "user2", "password": "1234" }
3) GET http://127.0.0.1:8000/api/v1/users/{id}/ Content-Type: application/json 
4) PUT http://127.0.0.1:8000/api/v1/users/{id}/ { "last_name": "LastName" } 
5) PATCH http://127.0.0.1:8000/api/v1/users/{id}/ { "first_name": "FirstName" } 
6) DELET http://127.0.0.1:8000/api/v1/users/{id}/
