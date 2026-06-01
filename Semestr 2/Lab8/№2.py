import pandas as pd

df = pd.read_csv('titanic.csv')

adults = df[df["Age"] >= 18]
print(f"Количество пассажиров которым больше 18: {len(adults)}")

women = df[df["Sex"] == "female"]
print(f"Количество пассажиров-женщин {len(women)}")

business = df[df["Pclass"] == 1]
print(f"Количество пассажиров первого класса: {len(business)}")

adult_women_business = df[(df["Age"] >= 18) & (df["Sex"] == "female") & (df["Pclass"] == 1)]
print(f"Количество женщин которым больше 18 и которые летят первым классом: {len(adult_women_business)}")