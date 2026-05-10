import pandas as pd
import matplotlib.pyplot as plt

# Charger le dataset
df = pd.read_csv("data/sales.csv", encoding="latin1")

# Afficher les premières lignes
print(df.head())

# Calcul ventes mensuelles
monthly_sales = df.groupby("MONTH_ID")["SALES"].sum()

# Graphique
monthly_sales.plot(kind="line")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()