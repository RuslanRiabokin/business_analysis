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

# Перетворення в datetime
data['request_time'] = pd.to_datetime(data['request_time'])
data['start_time'] = pd.to_datetime(data['start_time'])

# === 1. ГРАФІК НАКОПИЧЕННЯ ЗАПИТІВ ПРОТЯГОМ ДОБИ ===
data['request_hour'] = data['request_time'].dt.hour
cumulative_requests = data.groupby('request_hour').size().sort_index().cumsum()

plt.figure(figsize=(10, 5))
plt.plot(cumulative_requests.index, cumulative_requests.values, marker='o', color='purple')
plt.title('Накопичення запитів протягом доби')
plt.xlabel('Година доби')
plt.ylabel('Кумулятивна кількість запитів')
plt.grid(True)
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()

# === 2. ГРАФІК ЗАПИТІВ ЗА ДНЯМИ ТИЖНЯ ===
data['request_weekday'] = data['request_time'].dt.day_name()
data['start_weekday'] = data['start_time'].dt.day_name()

weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

request_by_day = data['request_weekday'].value_counts().reindex(weekday_order)
start_by_day = data['start_weekday'].value_counts().reindex(weekday_order)

plt.figure(figsize=(10, 5))
plt.bar(request_by_day.index, request_by_day.values, alpha=0.6, label='Надходження запитів', color='skyblue')
plt.bar(start_by_day.index, start_by_day.values, alpha=0.6, label='Обробка запитів', color='lightgreen')
plt.title('Розподіл запитів за днями тижня')
plt.xlabel('День тижня')
plt.ylabel('Кількість запитів')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
