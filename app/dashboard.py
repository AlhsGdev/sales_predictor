import streamlit as st

st.title("Sales Prediction App")

# INPUT utilisateur
prix = st.text_input("Prix (ex: 1 500 000)")
quantite = st.text_input("Quantité")
cout = st.text_input("Coût")

# CONVERSION en float propre
def clean_number(value):
    return float(value.replace(" ", "").replace(",", "."))

if st.button("Predict"):
    try:
        prix = clean_number(prix)
        quantite = clean_number(quantite)
        cout = clean_number(cout)

        st.write("Prix:", prix)
        st.write("Quantité:", quantite)
        st.write("Coût:", cout)

    except:
        st.error("Entre des nombres valides")