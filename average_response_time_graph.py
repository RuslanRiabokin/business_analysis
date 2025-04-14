import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Підключення до бази
conn = sqlite3.connect(r'D:\Users\user\Pycharm_new_Projects\business_analysis\moderator_data.db')

# SQL-запит
query = """
SELECT 
    DATE(request_time) AS day,
    ROUND(AVG(strftime('%s', start_time) - strftime('%s', request_time)) / 60.0, 2) AS avg_response_minutes
FROM 
    moderator_requests
WHERE 
    CAST(strftime('%H', request_time) AS INTEGER) BETWEEN 7 AND 22
    AND CAST(strftime('%H', start_time) AS INTEGER) BETWEEN 7 AND 22
    AND start_time IS NOT NULL
GROUP BY 
    DATE(request_time)
HAVING 
    COUNT(*) > 0
ORDER BY 
    DATE(request_time);
"""

# Завантаження
df = pd.read_sql(query, conn)
conn.close()

# Додаємо день тижня
df['day'] = pd.to_datetime(df['day'])
df['weekday'] = df['day'].dt.dayofweek  # 5 = субота, 6 = неділя

# Побудова графіка
plt.figure(figsize=(12, 6))
plt.plot(df['day'], df['avg_response_minutes'], color='steelblue', label='Середній час відповіді')

# Підсвітка вихідних днів
weekends = df[df['weekday'] >= 5]
plt.scatter(weekends['day'], weekends['avg_response_minutes'], color='orange', label='Вихідні дні', zorder=5)

# Підсвітка пікових значень (топ-3)
top_peaks = df.sort_values(by='avg_response_minutes', ascending=False).head(3)
plt.scatter(top_peaks['day'], top_peaks['avg_response_minutes'], color='red', label='Пікові значення', s=100, zorder=6)

# Підписи
plt.title('Середній час відповіді модераторів по днях', fontsize=14)
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Середній час відповіді (хв)', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
