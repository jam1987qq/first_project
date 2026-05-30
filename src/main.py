import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

def print_author():
    # Читаем значение переменной AUTHOR из окружения
    author = os.getenv("AUTHOR")
    print(f"Автор проекта: {author}")

if __name__ == "__main__":
    print_author()
