"""Flask-приложение: Hello World + Jinja2.

Задания средней сложности №1 и №9.
"""

from pathlib import Path

from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder=str(Path(__file__).parent / "templates"),
)


@app.route("/")
def hello() -> str:
    """Hello World (задание №1)."""
    return "Привет Flask!"


@app.route("/students")
def students():
    """Страница со списком студентов через Jinja2 (задание №9)."""
    data = [
        {"name": "Иванов Алексей", "group": "221341", "score": 4.5},
        {"name": "Петрова Мария", "group": "221341", "score": 4.8},
        {"name": "Сидоров Иван", "group": "221342", "score": 3.9},
        {"name": "Козлова Анна", "group": "221341", "score": 5.0},
    ]
    return render_template(
        "index.html",
        title="Список студентов",
        students=data,
        course="Методы и технологии программирования",
    )


if __name__ == "__main__":
    print("Flask: http://127.0.0.1:5000/")
    print("Jinja2: http://127.0.0.1:5000/students")
    app.run(debug=True)
