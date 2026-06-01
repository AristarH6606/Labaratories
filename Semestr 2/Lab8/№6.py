import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
clean_age = df['Age'].dropna()
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

#6.1 Гистограмма распределение возраста
plt.figure(figsize=(8, 5))
clean_age.plot(kind="hist", bins=20, edgecolor='black', alpha=0.7, color='skyblue')
plt.title("Распределение возраста пассажиров Титаника", fontsize=14)
plt.xlabel("Возраст (годы)", fontsize=12)
plt.ylabel("Количество пассажиров", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

#6.2 Доля выживших по полу
survival_by_sex = df.groupby("Sex")["Survived"].mean()

plt.figure(figsize=(6, 5))
survival_by_sex.plot(kind="bar", color=['lightcoral', 'lightblue'], edgecolor='black')
plt.title("Доля выживших пассажиров в зависимости от пола", fontsize=14)
plt.xlabel("Пол", fontsize=12)
plt.ylabel("Доля выживших", fontsize=12)
plt.ylim(0, 1)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Добавление значений на столбцы
for i, v in enumerate(survival_by_sex):
    plt.text(i, v + 0.02, f"{v:.2%}", ha='center', fontsize=11)

plt.show()

#6.3 Доля выживших по классу
survival_by_class = df.groupby("Pclass")["Survived"].mean()

plt.figure(figsize=(6, 5))
survival_by_class.plot(kind="bar", color=['skyblue', 'gold', 'silver'], edgecolor='black')
plt.title("Доля выживших пассажиров по классу обслуживания", fontsize=14)
plt.xlabel("Класс (Pclass)", fontsize=12)
plt.ylabel("Доля выживших", fontsize=12)
plt.ylim(0, 1)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)

for i, v in enumerate(survival_by_class):
    plt.text(i, v + 0.02, f"{v:.2%}", ha='center', fontsize=11)

plt.show()