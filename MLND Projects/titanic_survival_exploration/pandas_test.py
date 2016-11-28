import pandas as pd
titanic = pd.read_csv("titanic_data.csv")
print(titanic.head(5))
print(titanic.describe())
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())
print(titanic.describe())
