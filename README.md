# API Yatube
## Описание:
API для проекта социальной сети
## Установка:
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:falkky/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
```
source env/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

## Примеры запросов к API:
Endpoint:
```
api/v1/posts/{id}/
```
GET запрос:
```
api/v1/posts/1/
```
Ответ:
```
[
    {
      "id": 1,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
]
```
Endpoint:
```
api/v1/posts/{post_id}/comments/
```
POST запрос:
```
{
"text": "string"
}
```
Ответ:
```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```
