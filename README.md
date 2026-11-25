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

### Flask (задания №1 и №9)

```bash
python -m lab6.flask_app
```

Откройте http://127.0.0.1:5000/

### FastAPI (задания №6, №2↑, №9↑)

```bash
uvicorn lab6.fastapi_app:app --reload
```

Откройте http://127.0.0.1:8000/docs (Swagger UI)

## Структура

```text
lab6/
├── __init__.py
├── flask_app.py          # Flask Hello + Jinja2
├── fastapi_app.py         # FastAPI Hello + SQLAlchemy CRUD
├── database.py           # SQLAlchemy модели и сессия
└── templates/
    └── index.html        # Jinja2 шаблон
```
