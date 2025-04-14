import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Подключаемся к базе данных SQLite
connection = sqlite3.connect(r'D:\Users\user\Pycharm_new_Projects\business_analysis\moderator_data.db')

# Выполняем SQL-запрос
data = pd.read_sql("""
    SELECT moderator, team, 
           COUNT(DISTINCT DATE(start_time)) AS work_days, 
           COUNT(id_request) AS total_requests, 
           ROUND(1.0 * COUNT(id_request) / COUNT(DISTINCT DATE(start_time)), 2) AS avg_per_day
    FROM moderator_requests
    GROUP BY moderator, team
""", connection)

# Закрываем соединение
connection.close()

# Выводим результат
print(data)

# 1. Анализ средней активности
print(data['avg_per_day'].describe())

# 2. Визуализация количества запросов по командам
team_activity = data.groupby('team')['total_requests'].sum().sort_values(ascending=False)
team_activity.plot(kind='bar')
plt.title('Общее количество запросов по командам')
plt.xlabel('Команды')
plt.ylabel('Количество запросов')
plt.show()

# 3. Гистограмма для средней продуктивности
data['avg_per_day'].hist(bins=10)
plt.title('Распределение средней продуктивности')
plt.xlabel('Среднее количество запросов за день')
plt.ylabel('Частота')
plt.show()

# 4. Анализ зависимости между рабочими днями и количеством запросов
plt.scatter(data['work_days'], data['total_requests'])
plt.title('Зависимость рабочих дней от количества запросов')
plt.xlabel('Количество рабочих дней')
plt.ylabel('Общее количество запросов')
plt.show()
