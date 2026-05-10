import pandas as pd
import mysql.connector

# Charger dataset
df = pd.read_csv("data/sales.csv", encoding="latin1")

# Connexion MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TON_MOT_DE_PASSE",
    database="salesdb"
)

cursor = conn.cursor()

# Insertion simple
for _, row in df.iterrows():
    sql = """
    INSERT INTO sales(order_number, sales, quantity_ordered, price_each)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        str(row["ORDERNUMBER"]),
        float(row["SALES"]),
        int(row["QUANTITYORDERED"]),
        float(row["PRICEEACH"])
    )

    cursor.execute(sql, values)

conn.commit()

print("Données importées.")