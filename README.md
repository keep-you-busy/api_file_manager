# api_file_manager
example.env - пример файла .env.
## Запуск задания:
docker compose up -d
GET запрос (в postman, например):
http://localhost:8000/api/files/
POST запрос (с .txt файлом в поле file):
http://localhost:8000/api/files/upload/