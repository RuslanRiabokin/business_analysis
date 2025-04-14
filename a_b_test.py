import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Случайность, но с фиксированным seed для воспроизводимости
np.random.seed(42)

# Число пользователей в каждой группе
n_users = 10000

# Задаём реальную вероятность покупки для каждой группы
true_conv_rates = {
    'A': 0.05,
    'B': 0.065,
    'C': 0.06
}

# Симулируем: покупка (1) или нет (0)
data = {
    group: np.random.binomial(1, prob, n_users)
    for group, prob in true_conv_rates.items()
}

# Посчитаем конверсии
conversions = {group: np.mean(actions) for group, actions in data.items()}
print("Конверсии:")
for group, conv in conversions.items():
    print(f"{group}: {conv:.2%}")

# 📊 Построим график
sns.barplot(x=list(conversions.keys()), y=list(conversions.values()))
plt.ylabel('Конверсия')
plt.title('Конверсии по группам A/B/C')
plt.ylim(0, 0.08)
plt.show()

# 🧪 Статистическое сравнение: A vs B, A vs C, B vs C
def z_test(group1, group2):
    successes = [np.sum(data[group1]), np.sum(data[group2])]
    nobs = [n_users, n_users]
    z_stat, p_val = stats.proportions_ztest(successes, nobs)
    print(f"\n{group1} vs {group2}")
    print(f"Z-статистика: {z_stat:.2f}")
    print(f"P-значение: {p_val:.4f}")
    if p_val < 0.05:
        print("✅ Различия значимы")
    else:
        print("⚠️ Различия НЕ значимы")

# Сравнения
z_test('A', 'B')
z_test('A', 'C')
z_test('B', 'C')
