import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            chat_id INTEGER PRIMARY KEY,
            name TEXT,
            work TEXT,
            email TEXT,
            score INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_user(chat_id, name, work, email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (chat_id, name, work, email)
            VALUES (?, ?, ?, ?)
        ''', (chat_id, name, work, email))
        conn.commit()
        return True  # Успешное добавление
    except sqlite3.IntegrityError:
        return False  # Запись с таким chat_id уже существует
    finally:
        conn.close()

def update_score(chat_id, score):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users SET score = ? WHERE chat_id = ?
    ''', (score, chat_id))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users
    ''')
    users = cursor.fetchall()
    conn.close()
    return users
