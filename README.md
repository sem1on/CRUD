# Тестовое задание

Сделайте CRUD для юзеров с токен аутентификацией. 
Для примера можно взять https://emphasoft-test-assignment.herokuapp.com/swagger/

Для запуска приложения:
cd/путь_до_проекта
создать Superuser
python manage.py runserver

Примеры запросов через Postman: 
POST http://127.0.0.1:8000/api-token-auth/ { "username": "user1", "password": "1234" } 
POST http://127.0.0.1:8000/api/v1/users/ { "username": "user2", "password": "1234" }
GET http://127.0.0.1:8000/api/v1/users/{id}/ Content-Type: application/json 
PUT http://127.0.0.1:8000/api/v1/users/{id}/ { "last_name": "LastName" } 
PATCH http://127.0.0.1:8000/api/v1/users/{id}/ { "first_name": "FirstName" } 
DELET http://127.0.0.1:8000/api/v1/users/{id}/
