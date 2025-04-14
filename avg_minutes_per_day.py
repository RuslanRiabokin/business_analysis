import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Підключення до бази
conn = sqlite3.connect(r'D:\Users\user\Pycharm_new_Projects\business_analysis\moderator_data.db')

# SQL-запит
query = """
SELECT 
    moderator,
    COUNT(DISTINCT DATE(start_time)) AS work_days,
    ROUND(SUM(strftime('%s', finish_time) - strftime('%s', start_time)) / 60.0, 2) AS total_minutes,
    ROUND(SUM(strftime('%s', finish_time) - strftime('%s', start_time)) / 60.0 / COUNT(DISTINCT DATE(start_time)), 2) AS avg_minutes_per_day, 
    team
FROM 
    moderator_requests
WHERE 
    start_time IS NOT NULL
    AND finish_time IS NOT NULL
GROUP BY 
    moderator
HAVING 
    work_days >= 10
ORDER BY 
    avg_minutes_per_day DESC;
"""

# Завантаження
df = pd.read_sql(query, conn)
conn.close()

# Побудова графіка
plt.figure(figsize=(12, 6))

# Різні кольори для команд
colors = {'wholesale': 'blue', 'retail': 'green'}

# Створення стовпчикової діаграми
plt.bar(df['moderator'].astype(str), df['avg_minutes_per_day'], color=df['team'].map(colors))

# Підписи
plt.title('Середній час роботи модераторів по днях', fontsize=14)
plt.xlabel('Модератор', fontsize=12)
plt.ylabel('Середнє час роботи (хв)', fontsize=12)
plt.xticks(rotation=90)  # Поворот підписів на осі X для зручності читання
plt.tight_layout()

# Показати графік
plt.show()
