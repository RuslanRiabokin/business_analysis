import pandas as pd
import sqlite3

# Шлях до твого CSV-файлу
csv_path = 'file_2.csv'

# 1. Завантаження CSV з парсингом дат
df = pd.read_csv(csv_path, parse_dates=['request_time', 'start_time', 'finish_time'])

# 2. Переконаємося, що дати в правильному форматі
df['request_time'] = pd.to_datetime(df['request_time'])
df['start_time'] = pd.to_datetime(df['start_time'])
df['finish_time'] = pd.to_datetime(df['finish_time'])

# 3. Підключення до SQLite (створює файл, якщо не існує)
conn = sqlite3.connect('moderator_data.db')
cursor = conn.cursor()

# 4. Створення таблиці
cursor.execute('''
    CREATE TABLE IF NOT EXISTS moderator_requests (
        moderator INTEGER,
        id_request INTEGER,
        request_time TIMESTAMP,
        start_time TIMESTAMP,
        finish_time TIMESTAMP,
        team TEXT
    )
''')

# 5. Завантаження даних у SQL
df.to_sql('moderator_requests', conn, if_exists='append', index=False)

# 6. Закриття з'єднання
conn.commit()
conn.close()

print("✅ Дані успішно імпортовано до бази SQLite.")
