import sqlite3
import os

def initiate_db():
    # Если файл базы данных существует, удалим его
    if os.path.exists('products.db'):
        os.remove('products.db')

    # Подключение к новой базе данных (будет создана)
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # SQL запрос для создания таблицы Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    # Заполнение таблицы значениями из test_products
    test_products = [
        {"title": "Product1", "description": "Описание 1", "price": 100},
        {"title": "Product2", "description": "Описание 2", "price": 200},
        {"title": "Product3", "description": "Описание 3", "price": 300},
        {"title": "Product4", "description": "Описание 4", "price": 400}
    ]

    for product in test_products:
        cursor.execute('''
            INSERT INTO Products (title, description, price)
            VALUES (?, ?, ?)
        ''', (product["title"], product["description"], product["price"]))

    # Создание таблицы Users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    ''')

    # Сохранение изменений и закрытие подключения
    conn.commit()
    conn.close()

def get_all_products():
    # Подключение к базе данных
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # SQL запрос для получения всех продуктов
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()  # Получаем все записи

    # Закрытие подключения
    conn.close()

    return products

def add_user(username, email, age):
    # Подключение к базе данных
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Добавление нового пользователя с балансом 1000
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))

    # Сохранение изменений и закрытие подключения
    conn.commit()
    conn.close()

def is_included(username):
    # Подключение к базе данных
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Проверка, существует ли пользователь
    cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,))
    count = cursor.fetchone()[0]  # Получаем количество найденных пользователей

    # Закрытие подключения
    conn.close()

    return count > 0  # Возвращаем True, если пользователь существует, иначе - False

# Инициализация базы данных
initiate_db()