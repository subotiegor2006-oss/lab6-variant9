# Лабораторная работа №6

Субботин Егор Сергеевич, группа 221341, вариант 9, лабораторная №6.

## Задания варианта

Средняя сложность:

- №1 — Flask-приложение «Hello World»
- №6 — FastAPI «Hello»
- №9 — шаблон Jinja2 с данными

Повышенная сложность:

- №2 — FastAPI с базой данных
- №9 — подключение SQLAlchemy

## Зависимости

```bash
pip install -r requirements.txt
```

## Запуск

### Flask (№1 и №9)

```bash
python -m lab6.flask_app
```

- http://127.0.0.1:5000/ — Hello World
- http://127.0.0.1:5000/students — Jinja2-таблица студентов

### FastAPI (№6, №2↑, №9↑)

```bash
uvicorn lab6.fastapi_app:app --reload
```

- http://127.0.0.1:8000/ — Hello JSON
- http://127.0.0.1:8000/docs — Swagger UI
- CRUD: `/students` (GET, POST, PUT, DELETE)

## Примеры запросов

```bash
# Hello
curl http://127.0.0.1:8000/

# Создать студента
curl -X POST http://127.0.0.1:8000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Иванов", "group": "221341", "score": 4.5}'

# Список
curl http://127.0.0.1:8000/students
```

## Структура

```text
lab6/
├── __init__.py
├── flask_app.py       # Flask Hello + Jinja2
├── fastapi_app.py      # FastAPI Hello + CRUD
├── database.py        # SQLAlchemy модели и сессия
└── templates/
    └── index.html     # Jinja2 шаблон
```

## Кратко по заданиям

| № | Что сделано |
|---|-------------|
| 1 | Flask `/` → «Привет Flask!» |
| 6 | FastAPI `/` → `{"message": "Привет FastAPI!"}` |
| 9 | Jinja2 `/students` — таблица с данными |
| 2↑ | FastAPI CRUD студентов с SQLite |
| 9↑ | SQLAlchemy 2.0 модели + session |
