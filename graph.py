import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Підключення до бази
conn = sqlite3.connect('orders.db')

# Ваш SQL-запит
query = '''
WITH user_total_spend AS (
    SELECT 
        id_user,
        id_region,
        SUM(amount) AS total_spend
    FROM orders
    WHERE status = 'success'
    GROUP BY id_user, id_region
),
regional_avg AS (
    SELECT 
        id_user,
        id_region,
        total_spend,
        AVG(total_spend) OVER (PARTITION BY id_region) AS avg_spend_region
    FROM user_total_spend
)
SELECT 
    id_user,
    id_region,
    total_spend,
    avg_spend_region
FROM regional_avg
WHERE total_spend > avg_spend_region
'''

# Створюємо df
df = pd.read_sql(query, conn)
conn.close()

# Побудова графіка
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='avg_spend_region', y='total_spend', hue='id_region', style='id_region', s=100)
plt.plot([df['avg_spend_region'].min(), df['avg_spend_region'].max()],
         [df['avg_spend_region'].min(), df['avg_spend_region'].max()],
         color='red', linestyle='--', label='Лінія = середній ТС')
plt.title('Порівняння Total Spend користувача і середнього по регіону')
plt.xlabel('Середній Total Spend по регіону')
plt.ylabel('Total Spend користувача')
plt.legend()
plt.tight_layout()
plt.show()
