import pandas as pd

df = pd.read_csv('titanic.csv')

group = df.groupby(['Sex', 'Pclass'])
analysis = group.agg(
    survived = ('Survived', 'mean'),
    fare = ('Fare', 'mean'),
    age = ('Age', 'mean')
).reset_index()

print(f"Анализ выживаемости, стоимость билета и возраста по группам: {analysis}")