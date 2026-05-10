from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

import pandas as pd
import joblib

# Charger dataset
df = pd.read_csv("data/sales.csv")

print(df.head())

# Variables
X = df[["Lag1", "Lag2"]]
y = df["Revenue"]

# Séparation train/test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Création modèle
model = LinearRegression()

# Entraînement
model.fit(X_train, y_train)

# Prédictions
predictions = model.predict(X_test)

# Erreur
error = mean_absolute_error(y_test, predictions)

print("Erreur :", error)

# Sauvegarde
joblib.dump(model, "models/sales_prediction.pkl")

print("Modèle sauvegardé.")