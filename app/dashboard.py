import streamlit as st
import pandas as pd
import joblib
import os

# Charger modèle
model_path = os.path.join("models", "sales_prediction.pkl")
model = joblib.load(model_path) 

st.title("📊 Sales Prediction App")

# Choix du mode
mode = st.radio("Choisir une option :", ["Importer CSV", "Saisie manuelle"])

# =========================
# 🟢 MODE 1 : CSV
# =========================
if mode == "Importer CSV":
    file = st.file_uploader("Importer votre fichier CSV", type=["csv"])

    if file is not None:
        df = pd.read_csv(file)
        st.write("📄 Données importées :", df)

        if st.button("Prédire"):
            predictions = model.predict(df)
            df["Prediction"] = predictions
            st.write("📊 Résultats :", df)

# =========================
# 🟡 MODE 2 : MANUEL
# =========================
else:
    st.subheader("✍️ Saisie des données")

    lag1 = st.number_input("Lag1", value=0.0)
    lag2 = st.number_input("Lag2", value=0.0)

    input_df = pd.DataFrame([[lag1, lag2]], columns=["Lag1", "Lag2"])

    if st.button("Prédire"):
        prediction = model.predict(input_df)
        st.success(f"📈 Résultat : {prediction[0]}")