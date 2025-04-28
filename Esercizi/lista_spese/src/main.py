import sqlite3
import pandas as pd 

conn = sqlite3.connect("spese.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS spese (
                    id INTEGER PRIMARY KEY,
                    data TEXT,
                    importo REAL,
                    categoria TEXT)''')
conn.commit()

def aggiungi_spesa(data, importo, categoria):
    cursor.execute("INSERT INTO spese (data, importo, categoria) VALUES (?, ?, ?)", (data, importo, categoria))
    conn.commit()

def mostra_spese():
    df = pd.read_sql("SELECT * FROM spese", conn)
    print(df)

# Esempio di utilizzo
aggiungi_spesa("2025-04-28", 50.0, "Cibo")
aggiungi_spesa("2025-04-27", 20.0, "Trasporti")

mostra_spese()
