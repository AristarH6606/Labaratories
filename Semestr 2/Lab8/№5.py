import pandas as pd

df = pd.read_csv('titanic.csv')

print(f'Количество пропусков до обработки: {df.isnull().sum()}')

median_age = df['Age'].median()
df["Age"] = df['Age'].fillna(median_age)

mode_embarked = df['Embarked'].mode()[0]
df["Embarked"] = df['Embarked'].fillna(mode_embarked)
print(f"median age: {median_age}")
print(f"mode: {mode_embarked}")

df.drop('Cabin', axis=1, inplace=True)
print(f"Количество пропусков после обработки  {df.isnull().sum()}")