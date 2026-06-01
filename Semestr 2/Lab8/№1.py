import numpy as np
import pandas as pd

df = pd.read_csv("titanic.csv")

print(f"Первые 5 строк данных: {df.head()}")
print(f"Информация о DataFrame: {df.info()}")
print(f"Основные статистические показатели: {df.describe()}")

#Определение числовых и категориальных признаков
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(include=["string", "category"]).columns.tolist()
print(f"Числовые значения: {numerical_cols}")
print(f'Категориальные значения: {categorical_cols}')