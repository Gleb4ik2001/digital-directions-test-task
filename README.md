# 📝 Task Manager API

**Task Manager API** — это RESTful веб-сервис для управления задачами, разработанный на Django + Django REST Framework.

---

## 🚀 Возможности

### 👤 Пользователи:
- Регистрация: `username`, `email`, `password`
- JWT-аутентификация (выдача и обновление токенов)

### ✅ Задачи (Tasks):
- CRUD-операции: создание, чтение, обновление, удаление задач
- Поля: `title`, `description`, `status (new, in_progress, done)`, `due_date`
- Фильтрация по статусу
- Сортировка по сроку выполнения
- Поиск по заголовку задачи
- Автоматическая метка `is_overdue`, если срок задачи истёк и она не выполнена
- Логирование просроченных задач в консоль
- Поддержка тегов (по желанию)

---

## ⚙️ Установка

```bash
git clone https://github.com/Gleb4ik2001/digital-directions-test-task .
cd digital-directions-test-task
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 📦 Зависимости

- Python 3.8+
- Django 4.x / 5.x
- djangorestframework
- djangorestframework-simplejwt
- drf-yasg (для Swagger)

---

## 🔐 Аутентификация

JWT-токены:
```bash
POST /api/token/           # Получить токен
POST /api/token/refresh/   # Обновить токен
```

В заголовках запросов:
```
Authorization: Bearer <token>
```

---

## 🧪 Эндпоинты

```http
# Регистрация нового пользователя
POST /api/register/

# Получение JWT-токена
POST /api/token/

# Обновление JWT-токена
POST /api/token/refresh/

# Работа с задачами
GET    /api/tasks/               # Список задач (фильтрация, поиск, сортировка)
POST   /api/tasks/               # Создать задачу
PUT    /api/tasks/<id>/          # Обновить задачу
DELETE /api/tasks/<id>/          # Удалить задачу
```

### 🔍 Параметры запроса:

- `status`: фильтрация по статусу (`new`, `in_progress`, `done`)
- `search`: поиск по заголовку (`search=meeting`)
- `ordering`: сортировка по дате (`ordering=due_date`)

Пример:
```
GET /api/tasks/?status=new&search=report&ordering=-due_date
```

---

## 📊 Swagger UI

Документация автоматически доступна по адресу:

- Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Redoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

## ❗ Обработка ошибок

- `400 Bad Request`: Неверные входные данные
- `401 Unauthorized`: Отсутствует или неверный токен
- `404 Not Found`: Ресурс не найден
- `500 Internal Server Error`: Ошибка сервера

---

## 🧠 Структура проекта

Используется Feature-Based архитектура (отдельные Django-приложения для users, tasks и т.д.).

---

## 🗃️ ORM

Все операции с базой данных реализованы через Django ORM.

---

---

## 🤝 Автор

- Gleb Kalashnikov  
- Email: g.kalashnikovvv@gmail.com