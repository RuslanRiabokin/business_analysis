import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Подключаемся к базе данных SQLite
connection = sqlite3.connect(r'D:\Users\user\Pycharm_new_Projects\business_analysis\moderator_data.db')

# Выполняем SQL-запрос, чтобы получить время поступления и обработки запросов
data = pd.read_sql("""
    SELECT moderator, id_request, request_time, start_time
    FROM moderator_requests
""", connection)

# Закрываем соединение
connection.close()

# Преобразуем столбцы в формат datetime
data['request_time'] = pd.to_datetime(data['request_time'])
data['start_time'] = pd.to_datetime(data['start_time'])

# Строим точечный график
plt.figure(figsize=(10, 6))
plt.scatter(data['request_time'], data['start_time'], alpha=0.6, c='blue', label='Request vs Start Time')

# Настроим график
plt.title('Время поступления запросов vs Время обработки запросов')
plt.xlabel('Время поступления запроса')
plt.ylabel('Время начала обработки запроса')

# Добавим сетку для удобства
plt.grid(True)
plt.xticks(rotation=45)  # Повернуть метки оси X для лучшей читаемости

# Показать график
plt.show()
