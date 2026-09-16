import pandas as pd
import sqlite3
from pathlib import Path

# Find the project folder
project_folder = Path(__file__).resolve().parent.parent

# Read the transformed data
input_file = project_folder / "data" / "transformed_sales.csv"
df = pd.read_csv(input_file)

# Database location
database_path = project_folder / "data" / "retail.db"

# Connect to the database
connection = sqlite3.connect(database_path)

# Load data into SQLite
df.to_sql("sales", connection, if_exists="replace", index=False)

connection.close()

print("Load completed successfully!")
print("Rows loaded:", len(df))
print("Database:", database_path)
print("Table: sales")