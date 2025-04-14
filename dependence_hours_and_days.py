import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Підключення до бази даних
connection = sqlite3.connect(r'D:\Users\user\Pycharm_new_Projects\business_analysis\moderator_data.db')

# Завантаження даних
data = pd.read_sql("SELECT request_time, start_time FROM moderator_requests", connection)
connection.close()

# Перетворення в datetime
data['request_time'] = pd.to_datetime(data['request_time'])
data['start_time'] = pd.to_datetime(data['start_time'])

# Додаємо день тижня та годину
data['request_day'] = data['request_time'].dt.day_name()
data['request_hour'] = data['request_time'].dt.hour

data['start_day'] = data['start_time'].dt.day_name()
data['start_hour'] = data['start_time'].dt.hour

# Встановлюємо порядок днів тижня
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# === 1. HEATMAP — Надходження запитів ===
pivot_request = data.pivot_table(index='request_day', columns='request_hour', aggfunc='size', fill_value=0)
pivot_request = pivot_request.reindex(days_order)

plt.figure(figsize=(14, 6))
sns.heatmap(pivot_request, cmap='Blues', linewidths=0.5, annot=True, fmt='d')
plt.title('🔥 Надходження запитів: день тижня vs година доби')
plt.xlabel('Година')
plt.ylabel('День тижня')
plt.tight_layout()
plt.show()

# === 2. HEATMAP — Обробка запитів ===
pivot_start = data.pivot_table(index='start_day', columns='start_hour', aggfunc='size', fill_value=0)
pivot_start = pivot_start.reindex(days_order)

plt.figure(figsize=(14, 6))
sns.heatmap(pivot_start, cmap='Greens', linewidths=0.5, annot=True, fmt='d')
plt.title('✅ Обробка запитів: день тижня vs година доби')
plt.xlabel('Година')
plt.ylabel('День тижня')
plt.tight_layout()
plt.show()
