import pandas as pd
import sqlite3


csv_file = 'Task 1 - Лист1.CSV'
df = pd.read_csv(csv_file)


df['amount'] = df['amount'].astype(str).str.replace(',', '.', regex=False).astype(float)


df['date_created'] = df['date_created'].str.replace(' UTC', '', regex=False)
df['date_created'] = pd.to_datetime(df['date_created'], format='%Y-%m-%d %H:%M:%S')


conn = sqlite3.connect('orders.db')
df.to_sql('orders', conn, if_exists='replace', index=False)


print(pd.read_sql('SELECT * FROM orders LIMIT 5', conn))
conn.close()
