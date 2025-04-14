import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Підключення до бази даних
connection = sqlite3.connect(r'D:\Users\user\Pycharm_new_Projects\business_analysis\moderator_data.db')

# Завантаження даних
data = pd.read_sql("""
    SELECT moderator, id_request, request_time, start_time
    FROM moderator_requests
""", connection)
connection.close()

# Перетворення до формату datetime
data['request_time'] = pd.to_datetime(data['request_time'])
data['start_time'] = pd.to_datetime(data['start_time'])

# Витягуємо години
data['request_hour'] = data['request_time'].dt.hour
data['start_hour'] = data['start_time'].dt.hour

# Групуємо по годинам
request_hourly = data.groupby('request_hour').size().reindex(range(24), fill_value=0)
start_hourly = data.groupby('start_hour').size().reindex(range(24), fill_value=0)

# Нормалізація на кількість днів
unique_days = data['request_time'].dt.date.nunique()
request_hourly_avg = request_hourly / unique_days
start_hourly_avg = start_hourly / unique_days

# Різниця між запитами та обробками
difference = request_hourly_avg - start_hourly_avg

# Знаходимо пікові години
peak_request_hour = request_hourly_avg.idxmax()
peak_start_hour = start_hourly_avg.idxmax()

# Побудова графіка
plt.figure(figsize=(12, 6))
plt.plot(request_hourly_avg.index, request_hourly_avg.values, label='Надходження запитів', color='blue')
plt.plot(start_hourly_avg.index, start_hourly_avg.values, label='Обробка запитів', color='green')
plt.plot(difference.index, difference.values, label='Різниця (надходження - обробка)', color='red', linestyle='--')

# Підсвічування пікових годин
plt.axvline(x=peak_request_hour, color='blue', linestyle='--', alpha=0.3, label=f'Пік надходжень: {peak_request_hour}:00')
plt.axvline(x=peak_start_hour, color='green', linestyle='--', alpha=0.3, label=f'Пік обробки: {peak_start_hour}:00')

# Підписи
plt.title('Аналіз запитів та обробок за годинами доби')
plt.xlabel('Година доби (0–23)')
plt.ylabel('Середня кількість запитів')
plt.xticks(range(0, 24))
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
