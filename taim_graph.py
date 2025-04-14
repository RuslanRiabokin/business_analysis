import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Подключаемся к базе данных SQLite
connection = sqlite3.connect(r'D:\Users\user\Pycharm_new_Projects\business_analysis\moderator_data.db')

# Загружаем нужные данные
data = pd.read_sql("""
    SELECT moderator, id_request, request_time, start_time
    FROM moderator_requests
""", connection)
connection.close()

# Преобразуем в datetime
data['request_time'] = pd.to_datetime(data['request_time'])
data['start_time'] = pd.to_datetime(data['start_time'])

# Выделим часы из времени
data['request_hour'] = data['request_time'].dt.hour
data['start_hour'] = data['start_time'].dt.hour

# Строим график
plt.figure(figsize=(12, 6))

# Поступление запросов
plt.scatter(data['request_hour'], data.index, color='blue', alpha=0.4, label='Время поступления')

# Обработка запросов
plt.scatter(data['start_hour'], data.index, color='green', alpha=0.4, label='Время обработки')

# Настройки графика
plt.title('Сравнение времени поступления и обработки запросов по часам')
plt.xlabel('Час суток (0–23)')
plt.ylabel('Номер записи (условный)')
plt.legend()
plt.grid(True)
plt.xticks(range(0, 24))  # часы от 0 до 23

plt.show()
