### Описание проекта API_YATUBE:


В проекте реализован API для сервиса Yatube.
Присутствуют модели для постов, сообществ, комментариев и подписок.

- Представления реализованы на вьюсетах.
- Для аутентификации использованы JWT-токены. Реализовано библиотекой djoser
- У неаутентифицированных пользователей доступ к API только на чтение.

  __Исключение — эндпоинт /follow/:
  доступ к нему предоставляется только после аутентификации.__
- Аутентифицированным пользователям разрешено изменение и удаление своего контента;
  __в остальных случаях доступ предоставляется только для чтения.__

---

### Запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/viator3m/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
---

### Примеры запросов к API
POST-запрос на создание нового пользователя
```
POST localhost:8000/api/v1/users/
Content-Type: application/json

{
  "username": "example_user",
  "password": "example_password"
}
```
Пример ответа
```
{
    "email": "",
    "username": "test_user_4",
    "id": 5
}
```
---
POST-запрос на получение jwt-токена
```
POST localhost:8000/api/v1/jwt/create/
Content-Type: application/json

{
    "username": "example_user",
    "password": "example_password"
}
```
Пример ответа
```
{
    "refresh": "eyJ0eXAiO...",
    "access": "eyJ0eXAiOi..."
}
```
---
GET-запрос на получение всех постов
```
GET localhost:8000/api/v1/posts/
```
Пример ответа
```
[
  {
    "id": 1,
    "author": "admin",
    "text": "Test1",
    "pub_date": "2022-06-05T09:12:02.847270Z",
    "image": null,
    "group": 1
  },
]
```
---
POST-запрос на добавление публикации. В заголовке используется jwt-токен полученный под ключом ```access```
```
POST localhost:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer "eyJ0eXAiOi..."

{
  "text": "new_publication"
}
```
Пример ответа
```
{
  "id": 5,
  "author": "admin",
  "text": "new_publication",
  "pub_date": "2022-06-05T10:23:24.450095Z",
  "image": null,
  "group": null
}
```
