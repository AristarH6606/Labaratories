import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')

clean_age = df["Age"].dropna()
clean_fare = df["Fare"].dropna()

numpy_mean_age = np.mean(clean_age)
numpy_max_fare = np.max(clean_fare)
numpy_min_fare = np.min(clean_fare)

print("Результаты NumPy:")
print(f"Средний возраст (NumPy): {numpy_mean_age:.2f}")
print(f"Максимальная стоимость билета (NumPy): {numpy_max_fare:.2f}")
print(f"Минимальная стоимость билета (NumPy): {numpy_min_fare:.2f}")

# Использование Pandas (более удобный синтаксис)
pandas_mean_age = df['Age'].mean()
pandas_max_fare = df['Fare'].max()
pandas_min_fare = df['Fare'].min()

print("Результаты Pandas:")
print(f"Средний возраст (Pandas): {pandas_mean_age:.2f}")
print(f"Максимальная стоимость билета (Pandas): {pandas_max_fare:.2f}")
print(f"Минимальная стоимость билета (Pandas): {pandas_min_fare:.2f}")